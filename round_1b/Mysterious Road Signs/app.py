from pprint import pprint
import math
from collections import defaultdict


def rnd(l):
    if l % 1 >= 0.5:
        return math.ceil(l)
    return math.trunc(l)


T = int(input())
for t in range(T):
    S = int(input())
    L = []
    for s in range(S):
        D, A, B = map(int, input().split())
        L.append((D, A, B))

    max_set = 0
    max_set_count = 0

    for s1 in range(S):
        cur_set_count = 1
        D, A, B = L[s1]
        M = D + A
        N = D - B

        matchM = defaultdict(int)
        matchN = defaultdict(int)
        matchM[M] = 1
        matchN[N] = 1
        maxM = 1
        maxN = 1
        for s2 in range(s1 + 1, S):
            D, A, B = L[s2]
            M = D + A
            N = D - B
            matchM[M] += 1
            matchN[N] += 1
            if matchM[M] > maxM:
                maxM = matchM[M]
            if matchN[N] > maxN:
                maxN = matchN[N]
            if matchM[M] + maxN >= s2 - s1 + 1 or matchN[N] + maxM >= s2 - s1 + 1:
                cur_set_count += 1
                continue
            break
        if cur_set_count == max_set:
            max_set_count += 1
        elif cur_set_count > max_set:
            max_set = cur_set_count
            max_set_count = 1

    print('Case #' + str(t + 1) + ': ' + str(max_set) + ' ' + str(max_set_count))
