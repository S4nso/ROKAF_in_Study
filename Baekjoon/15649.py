#! /bin/usr/python3
from itertools import permutations

N, M = map(int, input().split())
P = permutations(range(1, N+1), M) # 1~ n까지 M개를 뽑아서

for i in P:
    print(' '.join(map(str, i)))
