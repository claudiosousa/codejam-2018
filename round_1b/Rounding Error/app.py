from pprint import pprint
import math

def rnd(l):
    if l % 1 >= 0.5:
        return math.ceil(l)
    return math.trunc(l)


T = int(input())
for i in range(T):
    N, L = map(int, input().split())
    langs = list(map(int, input().split()))
    percent = 100 / N

    done = sum(langs)
    langs = list(map(lambda l: l * percent, langs))
    langs.sort(key=lambda x: (x + 0.5) % 1, reverse=True)
    max_percent = sum(map(rnd, langs))

    N = N - done
    li = 0
    while N > 0:
        if li >= len(langs):
            langs.append(percent)
            N -= 1
        if N == 0:
            break
        while langs[li] % 1 < 0.5:
            langs[li] += percent
            N -= 1
            if N == 0:
                break
        li += 1
        if N == 0:
            break
        max_percent = max(max_percent, sum(map(rnd, langs)))
    max_percent = max(max_percent, sum(map(rnd, langs)))
    langs.append(1)

    print('Case #' + str(i + 1) + ': ' + str(max_percent))
