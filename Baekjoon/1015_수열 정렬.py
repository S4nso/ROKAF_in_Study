#! /bin/usr/python3
import sys
import math

n = int(input())
a = list(map(int, input().split()))
a_sort = [i for i in a]
a_sort.sort()
p = []

for i in a:
    p.append(a_sort.index(i))
    a_sort[a_sort.index(i)] = -1

re = [i for i in p]

for re in re:
    print(str(re)+' ')


'''--------------------------------------------'''
#! /bin/usr/python3

import sys
import math

A_size = int(sys.stdin.readline())
A = sys.stdin.readline().replace("\n", "").split(' ')
A = [int(i) for i in A]

sorted_A = [i for i in A]
sorted_A.sort()

P = []

for i in A:
    P.append(sorted_A.index(i))
    sorted_A[sorted_A.index(i)] = -1

results = [i for i in P]

for result in results:
    sys.stdout.write(str(result)+' ')
