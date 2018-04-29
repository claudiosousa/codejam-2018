from collections import defaultdict
T = int(input())
for i in range(T):
    D, P = input().split()
    D = int(D)
    harm_min = 0
    harm_level = 0
    harms = defaultdict(int)
    harm = 0
    for p in list(P):
        if p is 'C':
            harm_level += 1
        else:
            harm_min += 1
            harms[harm_level] += 1
            harm += 2**harm_level
    if harm_min > D:
        res = 'IMPOSSIBLE'
    else:
        res = 0
        while harm > D:
            for m in reversed(range(1, harm_level + 1)):
                if m in harms:
                    harm -= 2**m / 2
                    res += 1
                    harms[m - 1] += 1
                    harms[m] -= 1
                    if harms[m] == 0:
                        del harms[m]
                        harm_level -= 1
                    break

    print('Case #'+str(i+1)+': '+str(res))
