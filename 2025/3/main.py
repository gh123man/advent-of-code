#!/opt/homebrew/bin/python3

from lib import *
from functools import cache

f = open('input.txt', 'r')
lines = f.read().splitlines()

@cache
def findLargestRange(line, size):
    if size == 0 or len(line) == 0:
        return ""

    best = "0"
    for i, val in enumerate(line):
        result = val + findLargestRange(line[i+1:], size-1)
        if int(result) > int(best) and len(result) == size:
            best = result
    return best

part1 = 0
part2 = 0
for line in lines:
    part1 += int(findLargestRange(line, 2))
    part2 += int(findLargestRange(line, 12))

print(part1)
print(part2)