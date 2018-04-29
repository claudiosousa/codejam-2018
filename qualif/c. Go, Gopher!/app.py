from collections import defaultdict
import sys
from math import *

def handleTestCase():
    A = int(input())

    x = int(sqrt(A))
    while A / x != A // x:
        x -= 1
    y = int(A / x)
    xmin = 10
    xmax = xmin + x
    ymin = 10
    ymax = ymin + y
    done = set()
    for x in range(xmin, xmax):
        for y in range(ymin, ymax):
            while (x, y) not in done:

                i = min(max(xmin + 1, x + 1), xmax - 2)
                j = min(max(ymin + 1, y + 1), ymax - 2)
                print('{}  {}'.format(i, j))
                sys.stdout.flush()
                i, j = list(map(int, input().split()))

                if i == j == -1:
                    exit(-1)
                if i == j == 0:
                    return
                done.add((i, j))


T = int(input())
for j in range(T):
    handleTestCase()
