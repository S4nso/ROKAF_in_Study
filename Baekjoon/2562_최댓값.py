#! /bin/usr/python3


arr = []
m = [0]
cnt = 0

for i in range(9):
    a = int(input())
    arr.append(a)

for j in range(len(arr)):
    if m[0] < arr[j]:
        m[0] = arr[j]
        cnt = j+1   


print('{}\n{}'.format(m[0],cnt))
