
from random import randint

def compare_int(a: int, b: int):
    if a>b:
        return 1
    elif a<b:
        return -1
    else:
        return 0

min, max = 0, 10 
x, y = randint(min,max), randint(min,max)
result = compare_int(x,y)
print("Result of comparison two integers (%d ,%d):" % (x,y))
match result:
    case 1: print(str(x)+' is greater than '+str(y))
    case -1: print(str(x)+' is lower than '+str(y))
    case other: print(str(x)+' is equal to '+str(y))


