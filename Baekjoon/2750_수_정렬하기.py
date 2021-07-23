a = int(input())
arr = []
for i in range(a):
    b = int(input())
    arr.append(b)   
arr.sort()

for i in range(a):
    print(arr[i])
