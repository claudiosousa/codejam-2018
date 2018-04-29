from collections import defaultdict
import sys
from math import *

T = int(input())
for j in range(T):
    S = float(input())
    S_MAX = 2**(1 / 2)
    s = S_MAX
    c = a = 0
    b = pi / 4
    while abs(s - S) >= 1e-10:
        c = (a + b) / 2
        s = S_MAX * cos(c)
        if s > S:
            a = c
        else:
            b = c
    c = pi/4 - c

    print('Case #{}:'.format(j + 1))
    print('{} {} 0'.format(0.5*sin(c), 0.5*cos(c)))
    print('{} {} 0'.format(-0.5*cos(c), 0.5*sin(c)))
    print('0 0 0.5')
