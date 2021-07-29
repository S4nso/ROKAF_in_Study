num = int(input())

for i in range(num):
    n, s = input().split()
    for j in s:
        print(j*int(n), end='')
    print()
