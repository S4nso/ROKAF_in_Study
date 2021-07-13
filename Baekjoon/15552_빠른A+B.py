import sys
a = int(input())

for i in range(a):
    x,y = map(int,sys.stdin.readline().strip().split())
    print(x+y)
    
    
'''
input() -> 시간초과 -> sys.stdin.readline()사용
strip -> \n 개행문자 제거
'''
