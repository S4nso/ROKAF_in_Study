#조합
import itertools

k = [int(input()) for x in range(0,9)]

re = list(itertools.combinations(k, 7))
ap=[]
for i in re:
    s=0
    for j in i:
        s += j
        ap.append(j)
    if s == 100:
        result = sorted(ap, key=lambda x: x)
        for _ in result:
            print(_)
        break
    ap.clear()
            
'''

#부르트포스
heights = sorted([int(input()) for _ in range(9)])
sum_heights = sum(heights)

for i in range(8):
    for j in range(i + 1, 9):
        if sum_heights - (heights[i] + heights[j]) == 100:
            x1, x2 = heights[i], heights[j]

heights.remove(x1)
heights.remove(x2)

[print(h) for h in heights]


'''
