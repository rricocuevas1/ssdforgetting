from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from jaccard import *
from queue import PriorityQueue


def objective(dataset, dataset_prime_indices, queries, jaccard_sim=True):
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
                    similarity = jaccard(dataset.loc[d].values.flatten().tolist(), dataset.loc[d_prime].values.flatten().tolist())
                else:
                    similarity = cosine_similarity([dataset.loc[d].values.flatten().tolist()], [dataset.loc[d_prime].values.flatten().tolist()])[0][0]
                if similarity > best_similarity_d:
                    best_similarity_d = similarity
            partial_value = partial_value + (1 / len(answer_set_q_dataset))*best_similarity_d
        value = value + prob_q*partial_value
    return value


def lazy_greedy(dataset, queries, budget, jaccard_sim=True):
    # Priority queue implementation
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


'''
def greedy(dataset, queries, budget):
    timeout = time.time() + 60
    answer = []
    n = dataset.shape[0]
    for t in range(budget):
        if time.time() > timeout:
            return [-1]
        values = []
        for i in range(n):
            values.append(objective(dataset, list(set(answer).union({i})), queries) - objective(dataset, answer, queries))
        m = np.zeros(n, dtype=bool)
        m[answer] = True
        d_t = np.argmax(np.ma.array(values, mask=m))
        answer.append(d_t)
        """
        max_val, d_t = 0, 0
        for i in range(len(values)):
            if d_t in answer:
                d_t = d_t + 1
                continue
            elif values[i] >= max_val:
                max_val = values[i]
                d_t = i
        answer.append(d_t)
        """
    return answer


def lazy_greedy(dataset, queries, budget):
    answer = []
    n = dataset.shape[0]
    deltas = []
    for i in range(n):
        deltas.append([i, np.inf])
    for t in range(budget):
        curr = [True] * n
        for i in list(set(range(n)).difference(set(answer))):
            curr[i] = False
        while True:
            d_star_index = deltas[0][0]
            if curr[d_star_index]:
                answer.append(d_star_index)
                deltas.pop(0)
                break
            else:
                deltas[0][1] = objective(dataset, list(set(answer).union({d_star_index})), queries) - objective(dataset, answer, queries)
                deltas.sort(reverse=True, key=lambda x: x[1])
                if d_star_index == deltas[0][0]:
                    curr[d_star_index] = True
    return answer
'''
