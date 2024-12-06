#!/opt/homebrew/bin/python3 
from math import exp
from copy import copy, deepcopy
import re

f = open('input.txt', 'r')
lines = f.read().splitlines()

# up, right, down, left
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
#      y  x
pos = (0, 0)

def turn(currentDirection):
    return (currentDirection + 1) % len(directions)

def getCell(grid, position):
    if position[0] < 0 or position[1] < 0:
        return None
    try:
        return grid[position[0]][position[1]]
    except: 
        return None

mainGrid = []
for line in lines:
    mainGrid.append(list(line))

for y, row in enumerate(mainGrid):
    for x, v in enumerate(row):
        if v == "^":
            pos = (y, x)

def explore(grid, pos, paint):
    currentDirection = 0
    move = 1
    posCache = set()
    while True:
        if (pos, currentDirection) in posCache:
            return -1
        posCache.add((pos, currentDirection))
        if paint:
            grid[pos[0]][pos[1]] = "X"
        nextPos = (directions[currentDirection][0] + pos[0], directions[currentDirection][1] + pos[1])
        cell = getCell(grid, nextPos)
        if cell == None:
            return move
        elif cell == "#":
            currentDirection = turn(currentDirection)
            continue
        pos = nextPos
        if grid[pos[0]][pos[1]] != "X":
            move += 1
        

print(explore(deepcopy(mainGrid), pos, True))

print("It takes a while...")
loops = 0
for y, row in enumerate(mainGrid):
    for x, v in enumerate(row):
        if v == ".":
            # subgrid = deepcopy(mainGrid)
            mainGrid[y][x] = "#"
            if explore(mainGrid, pos, False) == -1:
                loops += 1
            mainGrid[y][x] = "."

print(loops)




