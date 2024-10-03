import random

import numpy as np


def pipage_rounding(x_fractional, n, B):
    """Randomized pipage rounding algorithm for matroid associated to the cardinality constraint"""
    p, q = 0, 1
    x = [round(i, 2) for i in x_fractional.copy()]
    if sum(x) != B:  # Normalize
        diff = B - sum(x)
        index = random.randrange(n)
        while x[index] == 0 or x[index] == 1:
            index = random.randrange(n)
        x[index] = x[index] + diff
    for t in range(n - 1):
        if p >= n or q >= n:
            return x
        elif x[p] == 0 or x[p] == 1:
            p = max((p, q)) + 1
        elif x[q] == 0 or x[q] == 1:
            q = max((p, q)) + 1
        elif x[p] + x[q] < 1:
            # This means that \alpha_x = min{1-x[p], x[q]} = x[q]
            #                 \beta_x  = min{1-x[q], x[p]} = x[p]
            # Consequently probability = \alpha_x/(\alpha_x + \beta_x) = x[q] / (x[p] + x[q])
            if np.random.rand() < x[q] / (x[p] + x[q]):
                x[q] = x[p] + x[q]
                x[p] = 0
                p = max((p, q)) + 1
            else:
                x[p] = x[p] + x[q]
                x[q] = 0
                q = max((p, q)) + 1
        else:
            # This means that \alpha_x = min{1-x[p], x[q]} = 1- x[p]
            #                 \beta_x  = min{1-x[q], x[p]} = 1- x[q]
            # Consequently probability = \alpha_x/(\alpha_x + \beta_x) = 1- x[p] / (2 - x[p] - x[q])
            if np.random.rand() < (1 - x[p]) / (2 - x[p] - x[q]):
                x[p] = x[p] + x[q] - 1
                x[q] = 1
                q = max((p, q)) + 1

            else:
                x[q] = x[p] + x[q] - 1
                x[p] = 1
                p = max((p, q)) + 1
    answer = np.where(x == 1)[0].tolist()
    return answer
