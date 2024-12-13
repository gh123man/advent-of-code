from collections import defaultdict

f = open('input.txt', 'r')
lines = f.read().splitlines()

# up, right, down, left
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

grid = []
for line in lines:
    grid.append(list(line))

def getCell(position):
    x, y = position
    if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[x]):
        return None
    return grid[x][y]

def neighbors(pos, id):
    for d in directions:
        next = (pos[0] + d[0], pos[1] + d[1])
        c = getCell(next)
        if c == None:
            yield None
        elif c == id:
            yield next
        else:
            yield None 


explored = set()
def explore(pos):
    id = getCell(pos)
    q = [pos]
    p = 0
    shape = set()
    while q != []:
        pos = q.pop()
        if pos in explored:
            continue
        explored.add(pos)
        shape.add(pos)
        for neighbor in neighbors(pos, id):
            if neighbor == None:
                p += 1
            else:
                q.append(neighbor)
    return (id, p, shape)

sum = 0
shapes = []
for y, row in enumerate(grid):
    for x, v in enumerate(row):
        if (y, x) not in explored:
            id, p, shape = explore((y, x))
            sum += p * len(shape)
            shapes.append(shape)

print("part1", sum)

def transpose(lines):
    transposed = []
    for y in range(len(lines[0])):
        row = []
        for x in range(len(lines)):
            row.append(lines[x][y])
        transposed.append(row)
    return transposed

shapeSides = defaultdict(int)
flipLookup = False # Ugly hack to avoid refactoring a ton of code

def addSideToShape(pos, count):
    if pos == None:
        return
    if flipLookup:
        pos = (pos[1], pos[0])
    for i, shape in enumerate(shapes):
        if pos in shape:
            shapeSides[i] += count
            return


def addSides():
    for y, row in enumerate(grid):
        upSide = 0
        downSide = 0
        lastId = None
        lastPos = None
        for x, id in enumerate(row):
            pos = (y, x)
            if lastId != None and id != lastId:
                addSideToShape(lastPos, upSide)
                addSideToShape(lastPos, downSide)
                upSide = 0
                downSide = 0
            
            dirs = list(neighbors(pos, id))
            up, down = dirs[0], dirs[2]
            if up == None:
                upSide = 1
            elif upSide == 1:
                addSideToShape(lastPos, upSide)
                upSide = 0
            if down == None:
                downSide = 1
            elif downSide == 1:
                addSideToShape(lastPos, downSide)
                downSide = 0
            lastId = id
            lastPos = pos
        if lastId != None:
            addSideToShape(lastPos, upSide)
            addSideToShape(lastPos, downSide)
            upSide = 0
            downSide = 0

addSides()
grid = transpose(grid)
flipLookup = True
addSides()

sum = 0
for k, v in enumerate(shapes):
    a = len(v)
    s = shapeSides[k]
    sum += a * s
        
print("part2", sum)

