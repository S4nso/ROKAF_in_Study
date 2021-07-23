a = list(map(int,input()))
n = len(a)
b = []
c = ''
for i in range(len(a)):
    b.extend(a[i:i+1:len(a)])

b.sort(reverse=True)
for j in range(n):
    c += str(b[j])

print(c)
