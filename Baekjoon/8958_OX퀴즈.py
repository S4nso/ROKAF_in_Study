'''num = int(input())
cnt = 0
for i in range(num):
    string = input()
    re = 0
    for j in string:
        if j == 'O':
            cnt += 1    
            re += cnt
        else:
            cnt = 0
    print(re)
'''
n = int(input())
for i in range(n):
    case = str(input())
    score = 0
    _count = 0
    for j in list(case):
        if j == "O":
            _count += 1
            score += _count
        elif j == "X":
            _count = 0
    print(score)
