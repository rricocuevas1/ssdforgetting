import numpy as np


def compute_frequency(n_rows, queries):
    frequency = np.zeros(n_rows, dtype=int)
    for j in range(len(queries)):
        answer_set = queries[j][0]
        np.add.at(frequency, answer_set, 1)
    return frequency


def query_based_amnesia(n_rows, budget, queries):
    """Query-based amnesia algorithm"""
    values = compute_frequency(n_rows, queries)
    values = values + float(1e-9)
    probabilities = values / np.sum(values)
    selected_indices = np.random.choice(len(values), size=budget, p=probabilities, replace=False)
    return selected_indices.tolist()
