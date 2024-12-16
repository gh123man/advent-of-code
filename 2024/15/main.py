from copy import copy, deepcopy
import posix

f = open('input.txt', 'r')
lines = f.read().splitlines()

# up, right, down, left
directions = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}

mainGrid = []
parseBoard = True
moves = ""
for line in lines:
    if parseBoard:
        mainGrid.append(list(line))
    else:
        moves += line
    if line == "":
        parseBoard = False

def getCell(board, position):
    x, y = position
    if x < 0 or y < 0 or x >= len(board) or y >= len(board[x]):
        return None
    return board[x][y]

def dump(board):
    for y, row in enumerate(board):
        for x, v in enumerate(row):
            print(v, end="")
        print()

def move(board, pos, next):
    v = board[pos[0]][pos[1]]
    board[pos[0]][pos[1]] = "."
    board[next[0]][next[1]] = v

def tryMove(board, pos, d):
    next = (pos[0] + d[0], pos[1] + d[1])
    if getCell(board, next) == "#":
        return pos 
    if getCell(board, next) == ".":
        move(board, pos, next)
        return next 
    if getCell(board, next) == "O":
        nn = tryMove(board, next, d)
        if nn != None and nn != next:
            move(board, pos, next)
            return next
        return pos

def explore(board, pos):
    for move in moves:
        direction = directions[move]
        pos = tryMove(board, pos, direction)

def tryUpBoxMove(board, nextl, nextr, charDir):
    cpy = deepcopy(board)
    nl = tryMove2(cpy, nextl, charDir)
    nr = tryMove2(cpy, nextr, charDir)
    if nl != None and nl != nextl and nr != None and nr != nextr:
        board[:] = cpy
        return True
    return False

def tryMove2(board, pos, charDir):
    d = directions[charDir]
    next = (pos[0] + d[0], pos[1] + d[1])
    if getCell(board, next) == "#":
        return pos 
    if getCell(board, next) == ".":
        move(board, pos, next)
        return next 
    if (charDir == ">" or charDir == "<") and (getCell(board, next) == "[" or getCell(board, next) == "]"):
        nn = tryMove2(board, next, charDir)
        if nn != None and nn != next:
            move(board, pos, next)
            return next
        return pos

    if (charDir == "^" or charDir == "v") and getCell(board, next) == "[":
        nextr = (next[0], next[1] + 1)
        if tryUpBoxMove(board, next, nextr, charDir):
            move(board, pos, next)
            return next
        return pos

    
    if (charDir == "^" or charDir == "v") and getCell(board, next) == "]":
        nextl = (next[0], next[1] - 1)
        if tryUpBoxMove(board, nextl, next, charDir):
            move(board, pos, next)
            return next
        return pos
    

def explore2(board, pos):
    for move in moves:
        pos = tryMove2(board, pos, move)

def score(grid):
    total = 0
    for y, row in enumerate(grid):
        for x, v in enumerate(row):
            if v == "O" or v == "[":
                total += (100 * y) + x
    return total

def findStart(grid):
    for y, row in enumerate(grid):
        for x, v in enumerate(row):
            if v == "@":
                return (y, x)
            

def enlarge(grid):
    newGrid = []
    for y, row in enumerate(grid):
        newRow = []
        for x, v in enumerate(row): 
            if v == "#":
                newRow += list("##")
            if v == "O":
                newRow += list("[]")
            if v == ".":
                newRow += list("..")
            if v == "@":
                newRow += list("@.")
        newGrid.append(newRow)
    return newGrid


part1 = deepcopy(mainGrid)
pos = findStart(part1)
explore(part1, pos)
print(score(part1))

part2 = enlarge(mainGrid)
pos = findStart(part2)
explore2(part2, pos)
print(score(part2))