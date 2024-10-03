import numpy as np


def compute_frequency(n_rows, queries):
    frequency = np.zeros(n_rows, dtype=int)
    for query in queries:
        np.add.at(frequency, query[0], 1)
    return frequency


def query_based_amnesia(n_rows, budget, queries):
    """Query-based amnesia algorithm"""
    values = compute_frequency(n_rows, queries) + 1e-9
    probabilities = values / np.sum(values)
    return np.random.choice(len(values), size=budget, p=probabilities, replace=False).tolist()
