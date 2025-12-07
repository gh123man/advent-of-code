#!/opt/homebrew/bin/python3

from lib import *
from collections import defaultdict
from functools import cache

f = open('input.txt', 'r')
lines = f.read().splitlines()

grid = Grid(lines)
start = grid.find("S")
beams = set([start])
splits = 0

adjList = defaultdict(list)

for i, row in enumerate(grid.board):
    if i == 0:
        continue
    newBeams = set()
    for beam in beams:
        b = (i, beam[1])
        if grid.get(b) == "^":
            splits += 1
            adjList[beam].append(b)
            for nextPos, _, _ in grid.neighbors(b, [cardinal_directions_map["W"], cardinal_directions_map["E"]]):
                newBeams.add(nextPos)
                adjList[b].append(nextPos)
        else:
            newBeams.add(b)
            adjList[beam].append(b)
    beams = newBeams

print(splits)

@cache
def dfs(node):
    if node not in adjList:
        return 1
    return sum(dfs(next) for next in adjList[node])

print(dfs(start))
