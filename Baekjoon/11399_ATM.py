a = int(input())
p = list(map(int,input().split()))
num = 0
p.sort()

for i in range(a+1):
    for j in range(i): 
        num += p[j] 
    m = num 

print(m)
