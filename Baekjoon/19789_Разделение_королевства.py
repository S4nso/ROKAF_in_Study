#! /bin/usr/python3

n = int(input())
 
a = list()
b = list()
x = set()
y = set()
for i in range(n):
    x1, y1 = map(int, input().split())
    a.append([x1, y1])
    b.append([y1, x1])
a.sort()
b.sort()
for i in range (n - 1):
    if a[i+1][0] == a[i][0] and a[i+1][1] > a[i][1]: # 같은 x 축에서 y가 더크면 y추가
        y.add(a[i][1] + 1)
    else:
        x.add(a[i][0] + 1)     #아니면 x
print(len(x) + len(y))
for i in x:
    print("x " + str(i))
for i in y:
    print("y " + str(i))

  
  
