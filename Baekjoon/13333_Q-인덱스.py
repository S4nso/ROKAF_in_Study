#! /bin/usr/python3

def solution(citations):
    answer = 0
    
    n = len(citations)
    
    citations.sort(reverse=True)
    
    for i in range(1,n+1):
        if i <= citations[i-1]:
            answer = i
    
    
    return answer
a=input()
n=list(map(int,input().split()))
print(solution(n))

# Hyper-index 문제
