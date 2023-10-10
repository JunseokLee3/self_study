from itertools import combinations

candidatate= list(combinations(chicken, m))

def get_sum(candidate):
    result = 0
    for hx, hy in house:
        temp = 1e9
        for cx, cy in candidate:
            temp = min(temp , abs(hx- cx) + abs(hy - cy))
        result += temp
    return result


