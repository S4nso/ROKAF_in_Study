x = int(input())
y = int(input())

def quadrant(x,y):
    
    if x > 0 and y > 0:
        print(1)
    elif x > 0 and y < 0:
        print(4)
    elif x < 0 and y > 0:
        print(2)
    else:
        print(3)
        
quadrant(x,y)
