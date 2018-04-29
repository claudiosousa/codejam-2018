from collections import defaultdict
T = int(input())
for j in range(T):
    N = int(input())
    Vs = list(map(int, input().split()))
    a = []
    b = []
    for i, e in enumerate(Vs):
        if i % 2:
            b.append(e)
        else:
            a.append(e)
    a.sort()
    b.sort()
    res = 'OK'
    for i in range(N - 1):
        i2 = i // 2
        if i % 2:
            if b[i2] > a[i2 + 1]:
                res = i
                break
        elif a[i2] > b[i2]:
            res = i
            break
    print('Case #{}: {}'.format(j + 1, res))
