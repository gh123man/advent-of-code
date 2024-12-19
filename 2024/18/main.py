from lib import *
import heapq
from collections import deque
import sys

lines = lines("input.txt")

w = 71
h = 71
end = (70, 70)

grid = Grid(lines=None, width=w, height=h, default=".")
data = []
for line in lines:
    x, y = line.split(",")
    data.append((int(y), int(x)))


for i in range(1024):
    grid.set(data[i], "#")


def bfs(end):
    q = [((0, 0), set())]
    seen = set()
    while q:
        next, steps = q.pop(0)
        if next == end: 
            return steps

        if next in seen: 
            continue
        seen.add(next)

        for nextPos, val, _ in grid.neighbors(next, cardinal_directions):
            if val == None or val == "#":
                continue
            s = steps.copy()
            s.add(nextPos)
            q.append((nextPos, s))
    return None

# Part 1
steps = bfs(end)
print(len(steps))

for i in range(2910): # skip ahead
    grid.set(data[i], "#")

for i in range(2910, len(data)):
    grid.set(data[i], "#")
    if bfs(end) == None:
        print(i, data[i][1], data[i][0])
        break
