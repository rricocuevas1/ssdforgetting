import numpy as np


def compute_frequency(n_rows, queries):
    weight = [0]*n_rows
    n_queries = len(queries)
    for i in range(n_rows):
        for j in range(n_queries):
            answer_set = queries[j][0]
            if i in answer_set:
                weight[i] = weight[i] + 1
    return weight


def query_based_amnesia(n_rows, budget, queries):
    epsilon = float(1e-9)
    values = compute_frequency(n_rows, queries)
    values = [value + epsilon for value in values]
    probabilities = values / np.sum(values)
    selected_indices = np.random.choice(len(values), size=budget, p=probabilities, replace=False)
    return selected_indices.tolist()