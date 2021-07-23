#! /bin/usr/python3
import sys
def solution(citations):
    answer = 0
    
    n = len(citations)
    
    citations.sort(reverse=True)
    
    for i in range(1,n+1):
        if i <= citations[i-1]:
            answer = i
    
    
    return answer
a = int(input())
n = list()
for i in range(a):
    n.append(int(sys.stdin.readline()))

print(solution(n))

#똑같은 문제 but sys모듈 사용해야함.
