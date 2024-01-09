import numpy as np


def compute_weight(n_rows, queries):
    weight = [0]*n_rows
    n_queries = len(queries)
    for i in range(n_rows):
        for j in range(n_queries):
            answer_set = queries[j][0]
            if i in answer_set:
                weight[i] = weight[i] + (queries[j][1])/(len(answer_set))
    return weight


def knapsack_solver(n_rows, budget, queries):
    values = compute_weight(n_rows, queries)
    return (np.argpartition(values, -budget)[-budget:]).tolist()
