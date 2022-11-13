import sys

def array(n,m):
    i = 1
    while True:
        print(i)
        i = 1 + (i + m - 2) % n
        if i == 1:
            break
    print()

array(int(sys.argv[1]),int(sys.argv[2]))
