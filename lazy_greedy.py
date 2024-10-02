from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pandas as pd
from jaccard import *
from queue import PriorityQueue


def objective(dataset, dataset_prime_indices, queries, jaccard_sim=True):
    # Convert the dataset to a NumPy array inside the function
    #if isinstance(dataset, pd.DataFrame):
    #    data_array = dataset.values  # Convert to NumPy array
    #else:
    data_array = dataset
    value = 0
    n_queries = len(queries)
    for q in range(n_queries):
        prob_q = queries[q][1]
        answer_set_q_dataset = queries[q][0]
        partial_value = 0
        for d in answer_set_q_dataset:
            best_similarity_d = 0
            answer_set_q_dataset_prime = list(set(answer_set_q_dataset).intersection(dataset_prime_indices))
            for d_prime in answer_set_q_dataset_prime:
                if jaccard_sim:
                    similarity = jaccard(
                        data_array[d],
                        data_array[d_prime]
                    )
                else:
                    similarity = cosine_similarity(
                        [data_array[d]],
                        [data_array[d_prime]]
                    )[0][0]
                    similarity = (similarity + 1) / 2
                if similarity > best_similarity_d:
                    best_similarity_d = similarity
            partial_value += (1 / len(answer_set_q_dataset)) * best_similarity_d
        value += prob_q * partial_value
    return value

def lazy_greedy(dataset, queries, budget, jaccard_sim=True):
    """Lazy Greedy algorithm for submodular optimization"""
    answer = []
    n = dataset.shape[0]
    deltas = PriorityQueue()
    for i in range(n):
        # (priority,index)
        deltas.put((-np.inf, i))
    for t in range(budget):
        curr = [True] * n
        for i in list(set(range(n)).difference(set(answer))):
            curr[i] = False
        while True:
            d_star_index = deltas.get()[1]
            if curr[d_star_index]:
                answer.append(d_star_index)
                break
            else:
                delta_d_star = -(objective(dataset, list(set(answer).union({d_star_index})), queries, jaccard_sim) - objective(dataset, answer, queries, jaccard_sim))
                deltas.put((delta_d_star, d_star_index))
                delta_top_of_q, index_top_of_q = deltas.get()
                if d_star_index == index_top_of_q:
                    curr[d_star_index] = True
                    deltas.put((delta_d_star, d_star_index))
                else:
                    deltas.put((delta_top_of_q, index_top_of_q))
    return answer

