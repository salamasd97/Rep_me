import math
import sys

def func(x,y,Rad,xk,yk):
    xk = int(xk)
    yk = int(yk)
    r_xy = math.sqrt(xk**2+yk**2)
    if (r_xy == Rad):
        return 0
    elif (x - xk) ** 2 / Rad ** 2 + (y - yk) ** 2 / Rad ** 2 < 1:
        return 1
    else:
        return 2

file_name1 = sys.argv[1]
file_name2 = sys.argv[2]

with open(file_name1,"r") as f:
    list_arg = [line.rstrip() for line in f.readlines()]
    x,y = list(map(int,((list_arg[0].split()))))
    Rad = int(list_arg[1])

with open(file_name2,"r") as f:
    list_cord = [line.rstrip() for line in f.readlines()]

for i in list_cord:
    print(func(x, y, Rad, i.split(" ")[0], i.split(" ")[1]))
