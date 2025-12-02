#!/opt/homebrew/bin/python3

from lib import *

f = open('input.txt', 'r')
line = f.read().splitlines()[0].split(",")

ranges = []

for l in line:
    ranges.append(range(int(l.split("-")[0]), int(l.split("-")[1]) + 1))

part1 = 0
part2 = 0

def checkSlice(s, size):
    return len(set([s[i:i+size] for i in range(0, len(s), size)])) == 1

for r in ranges:
    for i in r: 
        s = str(i) 
        left = s[:len(s) // 2]
        right = s[len(s) // 2:]
        if left == right:
            part1 += i

        for subIdx in range(int(len(s)/2)):
            endSlice = s[len(s) - subIdx - 1:]
            startSlice = s[:subIdx + 1]
            if endSlice == startSlice and checkSlice(s, subIdx + 1):
                part2 += i
                break

print(part1)
print(part2)