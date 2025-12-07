#!/opt/homebrew/bin/python3

from lib import *

f = open('input.txt', 'r')
lines = f.read().splitlines()

part1Lines = transpose([x.split() for x in lines])
part1 = 0
for line in part1Lines:
    op = line[0]
    res = int(line[1])
    for v in line[2:]:
        if op == "+":
            res += int(v)
        elif op == "*":
            res *= int(v)
    part1 += res
print(part1)

opts = lines[-1].split()[::-1]
lines = transpose([list(x) for x in lines[:-1]])
lines = ["".join(x[::-1]).strip() for x in lines]
lines.append("")

op = opts.pop()
acc = 0
part2 = 0
for line in lines:
    if line == "":
        part2 += acc
        acc = 0
        if opts:
            op = opts.pop()
        continue
    if acc == 0:
        acc = int(line) 
        continue
    if op == "+":
        acc += int(line)
    elif op == "*":
        acc *= int(line)

print(part2)