#! /bin/usr/python3

num = set()
for _ in range(10):
    i = int(input())
    num.add(i%42)

print(len(num))
