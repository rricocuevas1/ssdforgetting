def jaccard_optimised(d_1, d_2):
    set_1, set_2 = set(d_1), set(d_2)
    intersection = len(set_1 & set_2)
    union = len(set_1 | set_2)
    return intersection / union
