#!/opt/homebrew/bin/python3

f = open('3.txt', 'r')

grid = []
symb = set()
gearTable = {}

for line in f.read().splitlines():
    for c in line:
        if not c.isdigit() and c != ".":
            symb.add(c)
    grid.append(line)

def matches(x, y):
    match = ""
    try:
        match += grid[x + 1][y]
    except IndexError:
        pass
    try:
        match += grid[x - 1][y]
    except IndexError:
        pass
    try:
        match += grid[x][y + 1]
    except IndexError:
        pass
    try:
        match += grid[x][y - 1]
    except IndexError:
        pass
    try:
        match += grid[x + 1][y + 1]
    except IndexError:
        pass
    try:
        match += grid[x - 1][y - 1]
    except IndexError:
        pass
    try:
        match += grid[x - 1][y + 1]
    except IndexError:
        pass
    try:
        match += grid[x + 1][y - 1]
    except IndexError:
        pass
    
    return set(match) & symb

def hasGear(x, y):
    try:
        if grid[x + 1][y] == "*":
            return x + 1, y
    except IndexError:
        pass
    try:
        if grid[x - 1][y] == "*":
            return x - 1, y
    except IndexError:
        pass
    try:
        if grid[x][y + 1] == "*":
            return x, y + 1
    except IndexError:
        pass
    try:
        if grid[x][y - 1] == "*":
            return x, y - 1
    except IndexError:
        pass
    try:
        if grid[x + 1][y + 1] == "*":
            return x + 1, y + 1
    except IndexError:
        pass
    try:
        if grid[x - 1][y - 1] == "*":
            return x - 1, y - 1
    except IndexError:
        pass
    try:
        if grid[x - 1][y + 1] == "*":
            return x - 1, y + 1
    except IndexError:
        pass
    try:
        if grid[x + 1][y - 1] == "*":
            return x + 1, y - 1
    except IndexError:
        pass
    return None

def storeGear(gearCoords, num):
    if gearCoords not in gearTable:
        gearTable[gearCoords] = []
    gearTable[gearCoords].append(num)
    
s = 0
for x, line in enumerate(grid):

    numBuf = ""
    keep = False
    gearCoords = None
    for y, c in enumerate(line):
        if c.isdigit():
            numBuf+=c
            if not keep:
                keep = matches(x, y)
            if gearCoords == None:
                gearCoords = hasGear(x, y)
        else:
            if numBuf != "" and keep:
                s += int(numBuf)

            if numBuf != "" and gearCoords != None:
                storeGear(gearCoords, numBuf)
            numBuf = ""
            keep = False
            gearCoords = None
    if numBuf != "" and keep:
        s += int(numBuf)
    if numBuf != "" and gearCoords != None:
        storeGear(gearCoords, numBuf)

p2 = 0
for k, v in gearTable.items():
    v = list(v)
    if len(v) == 2:
        p2 += (int(v[0]) * int(v[1]))

print(s)
print(p2)