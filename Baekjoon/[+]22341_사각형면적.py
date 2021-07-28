'''
Y가 클때 세로로 자르고,
X가 클때 가로로 자른다.

자를때마다 좌표 수정하고 마지막때 X*Y면적 구하면됨.
'''
---------------20점짜리--------------------WHY?????????
#! /bin/usr/python3
N,C = map(int,input().split())

P = [N,N] # 사각형 생성

for i in range(C): # C만큼 반복
    x,y = map(int,input().split())
    
    if x > y: # x가 클때 세로로 자르기
        P[0] = x
    elif x < y: # y가 클때 가로로 자르기
        P[1] = y
    else: # x==y 일때 면적 큰걸로 자르기
        if x*P[1] < y*P[0]:
            P[1] = y
        else: # x*P[1] > y*P[0]:
            P[0] = x

            

result = P[0]*P[1]

print(result)
-----------------------------------------------
