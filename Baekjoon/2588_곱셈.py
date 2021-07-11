a = input()
b = input()

b = list(b)
n = 1
result = 0
for i in range(2,-1,-1):
    num = int(b[i])*int(a)
    print(num)
    result += num * n
    n *= 10

print(result)
