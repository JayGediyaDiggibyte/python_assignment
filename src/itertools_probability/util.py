from itertools import combinations

def probability_of_a(letters, k):
    combs = list(combinations(letters, k))

    favorable = sum(1 for comb in combs if 'a' in comb)
    return favorable / len(combs)