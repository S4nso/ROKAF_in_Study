n,m = map(int,input().split())
arr = list(map(int,input().split()))
x=0

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            y = arr[i]+arr[j]+arr[k]
            
            if y <= m:
                if abs(m-x) > abs(m-y):
                    x = arr[i]+arr[j]+arr[k]
                    
            if x == m: # Black Jack!!!
                print(x)
                exit()

print(x)

'''
왜 틀리지 >> 문제를 잘 읽자. m을 넘지 않는 선에서... y<=m 

'''
