import numpy as np
from itertools import islice
from multiprocessing import Pool, cpu_count

def chunked_iterable(iterable, chunk_size):
    it = iter(iterable)
    while True:
        chunk = list(islice(it, chunk_size))
        if not chunk:
            break
        yield chunk

def process_queries_chunk(args):
    n_rows, queries_chunk = args
    chunk_size = len(queries_chunk)
    weight_chunk = np.zeros(n_rows)
    for j in range(chunk_size):
        answer_set = queries_chunk[j][0]
        query_weight = queries_chunk[j][1]
        per_element_weight = query_weight / len(answer_set)
        np.add.at(weight_chunk, answer_set, per_element_weight)
    return weight_chunk

def compute_weight(n_rows, queries):
    weight = np.zeros(n_rows)
    n_queries = len(queries)
    n_cpus = min(cpu_count(), n_queries)
    if n_queries > 1000000 and n_rows > 10000000 and n_cpus > 1:
        chunk_size = (n_queries + n_cpus - 1) // n_cpus
        queries_gen = chunked_iterable(queries.values(), chunk_size)
        with Pool(n_cpus) as pool:
            results = pool.map(process_queries_chunk, [(n_rows, chunk) for chunk in queries_gen])
        for weight_chunk in results:
            weight += weight_chunk
    else:
        for j in range(n_queries):
            answer_set = queries[j][0]
            query_weight = queries[j][1]
            per_element_weight = query_weight / len(answer_set)
            np.add.at(weight, answer_set, per_element_weight)
    return weight

def indep_df(n_rows, budget, queries):
    """IndepDF algorithm"""
    values = compute_weight(n_rows, queries)
    top_indices = np.argpartition(values, -budget)[-budget:]
    return top_indices.tolist()
