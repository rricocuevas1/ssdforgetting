import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from jaccard import jaccard


def compute_similarity_matrix(data_array, answer_set_q, d, jaccard_sim):
    """Compute similarity vector"""
    if jaccard_sim:
        similarities = np.array([jaccard(d, data_array[i]) for i in answer_set_q])
    else:
        similarities = cosine_similarity([d], data_array[answer_set_q])[0]
    return similarities


def gradient(x, n, queries, p, m, data_array, K=20, jaccard_sim=True):
    """Compute the stochastic gradient"""
    q_index = np.random.choice(m, p=p)
    answer_set_q = queries[q_index][0]
    d_index = np.random.choice(answer_set_q)
    d = data_array[d_index]

    similarities = np.zeros(n)
    similarities[answer_set_q] = compute_similarity_matrix(data_array, answer_set_q, d, jaccard_sim)

    grad = np.zeros(n)
    for _ in range(K):
        D_prime = np.random.rand(n) < x
        answer_set_q_D_prime = np.intersect1d(np.where(D_prime)[0], answer_set_q)

        if answer_set_q_D_prime.size > 0:
            maximum = np.max(similarities[answer_set_q_D_prime])
        else:
            maximum = 0

        grad_contributions = np.maximum(0, similarities[answer_set_q] - maximum)
        grad[answer_set_q] += grad_contributions

    return grad / K


def largest_coordinates(d, n, B):
    """Select the B largest coordinates"""
    indices = np.argpartition(d, -B)[-B:]
    v = np.zeros(n, dtype=int)
    v[indices] = 1
    return v.tolist()


def scg(n, B, queries, p, m, dataset, T=500, K=20, jaccard_sim=True):
    """Stochastic Continuous Greedy algorithm for submodular optimization"""
    # Convert the dataset to a NumPy array inside scg
    # data_array = dataset.values  # Convert to NumPy array
    data_array = dataset
    d = np.zeros(n)
    x = np.zeros(n)
    ro_base = 1 / 2

    for t in range(T):
        ro = ro_base / ((t + 1) ** (2 / 3))
        grad = gradient(x, n, queries, p, m, data_array, K, jaccard_sim)  # Pass data_array
        d = d * (1 - ro) + grad * ro
        v = largest_coordinates(d, n, B)
        x += np.array(v) / T

    return x.tolist()
