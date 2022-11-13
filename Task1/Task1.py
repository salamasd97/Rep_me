import sys

def array(n,m):
    result = ""
    i = 1
    while True:
        result += str(i)
        i = 1 + (i + m - 2) % n
        if i == 1:
            break
    return result

print(array(int(sys.argv[1]),int(sys.argv[2])))
