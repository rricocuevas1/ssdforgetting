from collections import defaultdict
from itertools import combinations
from queue import PriorityQueue
import numpy as np
from datasketch import MinHash, MinHashLSH
from jaccard import jaccard
from sklearn.metrics.pairwise import cosine_similarity



# Helper functions for SimHash
def generate_random_hyperplanes(dim, num_bits):
    hyperplanes = np.random.randn(num_bits, dim)
    return hyperplanes


def compute_hash_codes(vectors, hyperplanes):
    projections = np.dot(vectors, hyperplanes.T)
    hash_codes = (projections >= 0).astype(np.uint8)
    return hash_codes


def build_hash_table(hash_codes):
    hash_table = defaultdict(list)
    for idx, code in enumerate(hash_codes):
        key = tuple(code)
        hash_table[key].append(idx)
    return hash_table


def query_hash_table(hash_table, query_code, max_hamming_distance=0):
    candidates = set()
    key = tuple(query_code)
    if key in hash_table:
        candidates.update(hash_table[key])
    # If allowing for Hamming distance > 0
    if max_hamming_distance > 0:
        for neighbor_code in generate_codes_within_hamming_distance(query_code, max_hamming_distance):
            neighbor_key = tuple(neighbor_code)
            if neighbor_key in hash_table:
                candidates.update(hash_table[neighbor_key])
    return list(candidates)


def generate_codes_within_hamming_distance(code, max_distance):
    n_bits = len(code)
    indices = range(n_bits)
    for distance in range(1, max_distance + 1):
        for bits_to_flip in combinations(indices, distance):
            new_code = code.copy()
            new_code[list(bits_to_flip)] ^= 1
            yield new_code


def create_lsh(dataset, threshold_acceptance=0.95, jaccard_sim=True):
    """Create LSH index using either MinHashLSH or SimHash"""
    data_array = dataset
    minhashes = {}
    if jaccard_sim:
        # Use MinHash for Jaccard similarity
        num_perm = 128
        threshold_acceptance = 0.95
        lsh = MinHashLSH(threshold=threshold_acceptance, num_perm=num_perm)
        for i in range(dataset.shape[0]):
            minhash = MinHash(num_perm=num_perm)
            for item in data_array[i]:
                minhash.update(str(item).encode('utf8'))
            lsh.insert(f'data_{i}', minhash)
            minhashes[i] = minhash
        return lsh, minhashes
    else:
        # Use SimHash for cosine similarity
        embedding_dim = dataset.shape[1]
        num_bits = int(np.floor(np.log2(len(dataset)))) + 1
        hyperplanes = generate_random_hyperplanes(embedding_dim, num_bits)
        hash_codes = compute_hash_codes(data_array, hyperplanes)
        hash_table = build_hash_table(hash_codes)
        lsh = (hyperplanes, hash_table)
        return lsh, None


def lsh_nn(lsh, minhashes, index, dataset, num_neighbors=10, jaccard_sim=True, subset_indices=[]):
    """Retrieve top-k nearest neighbors within a subset using LSH"""
    data_array = dataset
    if jaccard_sim:
        minhash = minhashes[index]
        similar_items = lsh.query(minhash)
        similar_items_indices = []
        for element in similar_items:
            parts = element.split('_')
            if len(parts) == 2 and parts[1].isdigit():
                idx = int(parts[1])
                if idx in subset_indices:
                    similar_items_indices.append(idx)
        if index in subset_indices:
            similar_items_indices.append(index)
        return similar_items_indices[:num_neighbors]
    else:
        # Use SimHash index for cosine similarity
        hyperplanes, hash_table = lsh
        vec = data_array[index]
        query_code = compute_hash_codes(vec.reshape(1, -1), hyperplanes)[0]
        similar_items = query_hash_table(hash_table, query_code, max_hamming_distance=0)
        similar_items = [idx for idx in similar_items if idx in subset_indices]
        return similar_items[:num_neighbors]


def objective_lsh(dataset, dataset_prime_indices, queries, lsh, minhashes, num_neighbors=10, jaccard_sim=True):
    """Objective function using LSH to speed up nearest neighbor search"""
    data_array = dataset
    value = 0
    n_queries = len(queries)
    for q in range(n_queries):
        prob_q = queries[q][1]
        answer_set_q_dataset = queries[q][0]  # q(D)
        partial_value = 0
        for d in answer_set_q_dataset:  # for d in q(D)
            best_similarity_d = 0
            answer_set_q_dataset_prime = list(set(answer_set_q_dataset).intersection(dataset_prime_indices))  # q(D')
            # Use the LSH index to not go through all q(D') (i.e., only compare with those elements in q(D') that are similar to d already)
            similar_items = lsh_nn(lsh, minhashes, d, dataset, num_neighbors, jaccard_sim,
                                   subset_indices=answer_set_q_dataset_prime)
            if len(similar_items) == 0:
                continue
            for d_prime in similar_items:
                if jaccard_sim:
                    similarity = jaccard(data_array[d], data_array[d_prime])
                else:
                    similarity = cosine_similarity([data_array[d]], [data_array[d_prime]])[0][0]
                    similarity = (similarity + 1) / 2
                if similarity > best_similarity_d:
                    best_similarity_d = similarity
            partial_value += (1 / len(answer_set_q_dataset)) * best_similarity_d
        value += prob_q * partial_value
    return value


def lazy_greedy_lsh(dataset, queries, budget, threshold_acceptance=0.9, num_neighbors=10, jaccard_sim=True):
    """Lazy greedy algorithm with LSH integration for submodular optimization"""
    lsh, minhashes = create_lsh(dataset, threshold_acceptance=threshold_acceptance, jaccard_sim=jaccard_sim)

    # Priority queue implementation
    answer = []
    n = dataset.shape[0]
    deltas = PriorityQueue()
    for i in range(n):
        # (priority,index)
        deltas.put((-np.inf, i))
    for t in range(budget):
        # print(f"Iteration {t}")
        curr = [True] * n
        for i in list(set(range(n)).difference(set(answer))):
            curr[i] = False
        while True:
            d_star_index = deltas.get()[1]
            if curr[d_star_index]:
                answer.append(d_star_index)
                # print(f"Included {d_star_index}")
                break
            else:
                delta_d_star = -(objective_lsh(
                    dataset,
                    list(set(answer).union({d_star_index})),
                    queries,
                    lsh,
                    minhashes,
                    num_neighbors,
                    jaccard_sim
                ) - objective_lsh(
                    dataset,
                    answer,
                    queries,
                    lsh,
                    minhashes,
                    num_neighbors,
                    jaccard_sim
                ))
                deltas.put((delta_d_star, d_star_index))
                delta_top_of_q, index_top_of_q = deltas.get()
                if d_star_index == index_top_of_q:
                    curr[d_star_index] = True
                    deltas.put((delta_d_star, d_star_index))
                else:
                    deltas.put((delta_top_of_q, index_top_of_q))
    return answer
