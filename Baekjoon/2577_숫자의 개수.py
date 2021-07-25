#! /bin/usr/python3

arr = []

for i in range(3):
    arr.append(int(input()))

num = arr[0]*arr[1]*arr[2]

re = list(map(int, str(num)))

for i in range(10):
    print(re.count(i))
