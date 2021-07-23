a = int(input())
arr = []
for i in range(a):
    b = int(input())
    arr.append(b)   
arr.sort()

for i in range(a):
    print(arr[i])
    

# 시간초과




import sys
n = int(input())
l = []
for i in range(n):
    l.append(int(sys.stdin.readline()))
for i in sorted(l):
    sys.stdout.write(str(i)+'\n')
