#!/opt/homebrew/bin/python3 
import enum
import itertools
from re import A

f = open('input.txt', 'r')
lines = f.read().splitlines()

grid = []
for line in lines:
    grid.append(list(line))


signals = {}

for y, row in enumerate(grid):
    for x, v in enumerate(row):
        if v != ".":
            if v not in signals:
                signals[v] = [(y, x)]
            else:
                signals[v].append((y, x))

def boundsCheck(p):
    return p[0] >= 0 and p[0] < len(grid) and p[1] >= 0 and p[1] < len(grid[0])

def getVecList(p1, p2):
    dy = p1[0] - p2[0]
    dx = p1[1] - p2[1]
    
    out = []
    while boundsCheck(p1):
        out.append(p1)
        p1 = (p1[0] + dy, p1[1] + dx)

    while boundsCheck(p2):
        out.append(p2)
        p2 = (p2[0] - dy, p2[1] - dx)
    return out

def getVecPair(p1, p2):
    dy = p1[0] - p2[0]
    dx = p1[1] - p2[1]
    v1 = (p1[0] + dy, p1[1] + dx)
    v2 = (p2[0] - dy, p2[1] - dx)
    return (v1, v2)
    
antiSignals = set()
antiSignals2 = set()
for signal, points in signals.items():
    for p1, p2 in itertools.combinations(points, 2):
        (v1, v2) = getVecPair(p1, p2)
        if boundsCheck(v1):
            antiSignals.add(v1)
        if boundsCheck(v2):
            antiSignals.add(v2)
        for p in getVecList(p1, p2):
            antiSignals2.add(p)

print(len(antiSignals))
print(len(antiSignals2))



