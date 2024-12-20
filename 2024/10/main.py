#!/opt/homebrew/bin/python3 
from re import A

f = open('input.txt', 'r')
lines = f.read().splitlines()

# up, right, down, left
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

grid = []
for line in lines:
    grid.append(list(line))

def getCell(grid, position):
    if position[0] < 0 or position[1] < 0:
        return None
    try:
        v = grid[position[0]][position[1]]
        if v == ".":
            return None
        return int(v)
    except: 
        return None

def neighbors(pos):
    v = getCell(grid, pos)
    for d in directions:
        newPos = (pos[0] + d[0], pos[1] + d[1])
        cell = getCell(grid, newPos)
        if cell != None and cell == v + 1:
            yield newPos

def explore(pos, new, append):
    if getCell(grid, pos) == 9:
        return new(pos)
    res = new()
    for n in neighbors(pos):
        append(res, explore(n, new, append))
    return res

score = 0
paths = 0
for y, row in enumerate(grid):
    for x, v in enumerate(row):
        if v == '0':
            score += len(explore((y, x), lambda *v: set(v), lambda x, y: x.update(y)))
            paths += len(explore((y, x), lambda *v: list(v), lambda x, y: x.extend(y)))

print(score)
print(paths)

