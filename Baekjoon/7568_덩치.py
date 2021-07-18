N = int(input())

people = []
for _ in range(N):
    w, h = map(int, input().split())
    people.append((w, h))

for c in people :
    rank = 1 
    
    for n in people:
        if (c[0]!=n[0]) & (c[1]!=n[1]): #2  
            if (c[0]<n[0]) & (c[1]<n[1]): #3 w, h 모두 큰 경우
                rank += 1
            
    print(rank)
