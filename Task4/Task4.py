import sys

file_name1 = sys.argv[1]
with open(file_name1,"r") as f:
    list_arg = list(map(int,[line.rstrip() for line in f.readlines()]))


def median(sample):
    n = len(sample)
    index = n // 2
    if n % 2:
        return sorted(sample)[index]
    return sum(sorted(sample)[index - 1:index])

x = median(list_arg)
total = 0
for i in list_arg:
    total += abs(i-x)

print(total)
