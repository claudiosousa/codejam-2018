from pprint import pprint
import math
from collections import defaultdict

class Metal():
    def __init__(self, m):
        self.m = m
        self.getting = False
        self.l = None
        self.r = None

    def getOne(self):
        if self.getting:
            return False
        if self.m > 0:
            self.m -= 1
            return True
        if self.l is None or self.r is None:
            return False
        self.getting = True
        res = self.l.getOne() and self.r.getOne()
        self.getting = False
        return res


T = int(input())
for t in range(T):
    M = int(input()) - 1
    formulas = []
    for m in range(M + 1):
        m1, m2 = map(int, input().split())
        if m1 == 1 or m2 == 1:
            continue
        formulas.append((m, m1-1, m2-1))

    metals = list(map(Metal, map(int, input().split())))

    for m, m1, m2 in formulas:
        metals[m].l = metals[m1]
        metals[m].r = metals[m2]

    lead = 0
    while metals[0].getOne():
        lead+=1

    print('Case #' + str(t + 1) + ': ' + str(lead))
