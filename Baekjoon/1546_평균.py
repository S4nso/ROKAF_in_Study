#! /bin/usr/python3
r = int(input())

a = list(map(int,input().split()))

print((sum(a)/r)/max(a)*100)
