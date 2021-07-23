#! /bin/usr/python3

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
    n.append(int(input()))

print(solution(n))

#똑같은 문제 but 시간초과
