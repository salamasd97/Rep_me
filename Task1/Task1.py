import sys

def array(n,m):
    i = 1
    while True:
        print(i)
        i = 1 + (i + m - 2) % n
        if i == 1:
            break
    print()

array(sys.argv[1],sys.argv[2])