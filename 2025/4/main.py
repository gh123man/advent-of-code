#!/opt/homebrew/bin/python3

from lib import *

f = open('input.txt', 'r')
grid = Grid(f.read().splitlines())

def countUnderFour(y, x):
    if grid.get((y, x)) != "@":
        return False
    return len([v for _, v, _ in grid.neighbors((y, x), all_edges) if v != None and v != "."]) < 4

part1 = 0
for y, x in grid.enumerate():
    if countUnderFour(y, x):
        part1 += 1

part2 = 0
while True:
    removed = False
    for y, x in grid.enumerate():
        if countUnderFour(y, x):
            grid.set((y, x), ".")
            removed = True
            part2 += 1
    if not removed:
        break

print(part1)
print(part2)