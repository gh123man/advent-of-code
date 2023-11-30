#!/opt/homebrew/bin/python3
from collections import defaultdict
import math

f = open('12.txt', 'r')

grid = []
for line in f.read().splitlines():
    grid.append([c for c in line])

height = len(grid)
width = len(grid[0])

def neighbors1(cords, grid):
    v = grid[cords[0]][cords[1]]
    if v == "S":
        v = "a"
    n = []
    if cords[0] + 1 < height:
        nv = grid[cords[0] + 1][cords[1]]
        if nv == "E":
            nv = "z"
        if (ord(nv) - ord(v) <= 1):
            n.append(((cords[0] + 1, cords[1]), nv))
    if cords[0] - 1 >= 0:
        nv = grid[cords[0] - 1][cords[1]]
        if nv == "E":
            nv = "z"
        if (ord(nv) - ord(v) <= 1):
            n.append(((cords[0] - 1, cords[1]), nv))
    if cords[1] + 1 < width:
        nv = grid[cords[0]][cords[1] + 1]
        if nv == "E":
            nv = "z"
        if (ord(nv) - ord(v) <= 1):
            n.append(((cords[0], cords[1] + 1), nv))
    if cords[1] - 1 >= 0:
        nv = grid[cords[0]][cords[1] - 1]
        if nv == "E":
            nv = "z"
        if (ord(nv) - ord(v) <= 1):
            n.append(((cords[0], cords[1] - 1), nv))
    return n

def neighbors2(cords, grid):
    v = grid[cords[0]][cords[1]]
    if v == "E":
        v = "z"
    n = []
    if cords[0] + 1 < height:
        nv = grid[cords[0] + 1][cords[1]]
        if nv == "E":
            nv = "z"
        if (ord(v) - ord(nv) <= 1):
            n.append(((cords[0] + 1, cords[1]), nv))
    if cords[0] - 1 >= 0:
        nv = grid[cords[0] - 1][cords[1]]
        if nv == "E":
            nv = "z"
        if (ord(v) - ord(nv) <= 1):
            n.append(((cords[0] - 1, cords[1]), nv))
    if cords[1] + 1 < width:
        nv = grid[cords[0]][cords[1] + 1]
        if nv == "E":
            nv = "z"
        if (ord(v) - ord(nv) <= 1):
            n.append(((cords[0], cords[1] + 1), nv))
    if cords[1] - 1 >= 0:
        nv = grid[cords[0]][cords[1] - 1]
        if nv == "E":
            nv = "z"
        if (ord(v) - ord(nv) <= 1):
            n.append(((cords[0], cords[1] - 1), nv))
    return n

def start(p):
    for y in range(height):
        for x in range(width):
            if grid[y][x] == p:
                return ((y, x), p)



def solve(f, start, ep):
    fromMap = {}
    queue = [start]
    done = False
    seen = set()
    end = ()
    while not done:
        cur = queue.pop()
        if grid[cur[0][0]][cur[0][1]] == ep:
            done = True
            end = cur[0]
            break

        for n in f(cur[0], grid):
            if n[0] in seen:
                continue

            seen.add(n[0])
            fromMap[n[0]] = cur[0]
            queue.insert(0, n)

    minLen = 0
    while True:
        if end == start[0]:
            break
        end = fromMap[end]
        minLen += 1
    print(minLen)


solve(neighbors1, start("S"), "E")
solve(neighbors2, start("E"), "a")