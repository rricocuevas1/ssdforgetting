import numpy as np
import csv
from jaccard import *
from sklearn.metrics.pairwise import cosine_similarity


def gradient(x, n, queries, p, m, dataset, K=20, jaccard_sim=True):
    # Sample q according to \mathcal{Q}
    q_index = np.random.choice(m, 1, p=p)[0]
    # Retrieve q(D)
    answer_set_q = queries[q_index][0]
    # Sample d uniformly at random from q(D)
    d_index = np.random.choice(answer_set_q, 1)[0]
    d = dataset.loc[d_index].values.flatten().tolist()
    #d = dataset.loc[dataset['id'] == 'Q1'].values.flatten().tolist()[1:] for Wikidata
    similarities = [0]*n
    for i in answer_set_q:
        d_i = dataset.loc[i].values.flatten().tolist()
        if jaccard_sim:
            similarities[i] = (jaccard(d, d_i))
        else:
            similarities[i] = cosine_similarity([d], [d_i])[0][0]
    # Repeat K times
    grad = [0] * n
    for t in range(K):
        # Sample D' = D_prime as indicated by x
        D_prime = []
        for i in range(n):
            if np.random.rand() < x[i]:
                D_prime.append(i)
        answer_set_q_D_prime = list(set(D_prime).intersection(answer_set_q))
        # Compute each \partial F_{q,d}(x) / \partial x_i = f_{q,d}(D'u{i}) - f_{q,d}(D'-{i})
        for i in answer_set_q:
            answer_set_q_D_prime_minus_i = answer_set_q_D_prime.copy()
            if i in answer_set_q_D_prime:
                answer_set_q_D_prime_minus_i.remove(i)
            maximum = 0
            for j in answer_set_q_D_prime_minus_i:
                temp = similarities[j]
                if maximum < temp:
                    maximum = temp
            grad[i] = grad[i] + max(0, similarities[i] - maximum)
    return [(1/K) * j for j in grad]


def largest_coordinates(d, n, B):
    """
    Given a vector d compute vector v. Vector v is an integral vector of
    n-B zeros and B ones where the ones correspond to the largest components of
    d. That is, v is the binary vector containing B ones that indicate the largest
    B components of d. eg: for input d=[1,2,1,5] , n = 4 , B = 2, the output would be
    v = [0,1,0,1]. Function np.argpartition() takes O(n) time and the loop has B iterations.
    Hence, largest_coordinates() takes O(n+B) = O(n) time to compute vector v.
    """
    v = [0] * n
    indices = np.argpartition(d, -B)[-B:]
    for i in indices:
        v[i] = 1
    return v


def scg(n, B, queries, p, m, dataset, T=500, K=20, jaccard_sim=True):
    d, x = [0] * n, [0] * n
    for t in range(T):
        ro = 1/(2 * ((t+1)**(2/3)))
        d = [sum(i) for i in zip([j * (1-ro) for j in d], [m * ro for m in gradient(x, n, queries, p, m, dataset, K, jaccard_sim)])]
        v = largest_coordinates(d, n, B)
        x = [sum(i) for i in zip(x, [(1/T) * j for j in v])]
    return x
