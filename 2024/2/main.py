#!/opt/homebrew/bin/python3

from collections import defaultdict
from tabnanny import check

f = open('input.txt', 'r')
lines = f.read().splitlines()

part2 = True
    
def validate(l):
    increasing = l[0] - l[1] < 0
    for i in range(len(l) - 1):
        diff = l[i] - l[i+1]
        if abs(diff) > 3 or abs(diff) <= 0:
            return False
        if increasing and diff > 0:
            return False
        elif not increasing and diff < 0:
            return False
    return True

count = 0
for line in lines:
    l = [int(v) for v in line.split()]

    if validate(l):
        count += 1
    elif part2:
        for i in range(len(l)):
            if validate(l[:i] + l[i+1:]):
                count += 1
                break

print(count)

