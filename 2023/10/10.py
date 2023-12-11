#!/opt/homebrew/bin/python3

f = open('10.txt', 'r')
board = f.read().splitlines()
paths = "|-LJ7F"
turns = "LJ7F"
          #  URDL
upDirs    = " F 7"
downDirs  = " L J"
rightDirs = "J 7 "
leftDirs  = "L F "
redirects = [upDirs, rightDirs, downDirs, leftDirs]
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

pathBoard = [["."] * 3 * len(board[0]) for _ in range(len(board) * 3)]

def pb(b):
    for r in b:
        print("".join(r))

def neighbors(x, y, board):
    tiles = []
    positions = []
    for (dx, dy) in directions:
        if x + dx >= 0 and x + dx < len(board) and y + dy >= 0 and y + dy < len(board[0]):
            tiles.append(board[x + dx][y + dy])
            positions.append((x + dx, y + dy))
        else:
            tiles.append(".")
            positions.append(None)
    return tiles, positions

def findStart():
    for x, a in enumerate(board):
        for y, b in enumerate(a):
            if b == "S":
                return (x, y)

def findFirstPosition(startNeighbors):
    for i, n in enumerate(startNeighbors):
        if n in paths and n in redirects[i]:
            return i
        if n in "|-":
            return i

def extendLine(nextPos, direction):
    newDir = (directions[direction][0], directions[direction][1])
    pathBoard[nextPos[0] * 3][nextPos[1] * 3] = "X"
    pathBoard[(nextPos[0] * 3) + (newDir[0] * 1)][(nextPos[1] * 3) + (newDir[1] * 1)] = "X"
    pathBoard[(nextPos[0] * 3) + (newDir[0] * 2)][(nextPos[1] * 3) + (newDir[1] * 2)] = "X"

moves = 0
nextPos = findStart()
startNeighbors, _ = neighbors(*nextPos, board)
direction = findFirstPosition(startNeighbors)
extendLine(nextPos, direction)

while True:
    moves += 1
    newDir = (directions[direction][0], directions[direction][1])
    nextPos = (nextPos[0] + directions[direction][0], nextPos[1] + directions[direction][1])
    next = board[nextPos[0]][nextPos[1]]

    if next == "S":
        break

    if next in turns:
        direction = redirects[direction].index(next)
        newDir = (directions[direction][0], directions[direction][1])

    extendLine(nextPos, direction)

# Part 1
print(int(moves / 2))
assert 6867 == int(moves / 2)

def color(x, y, c):
    q = [(x, y)]
    count = 0
    while q:
        p = q.pop()
        x = p[0]
        y = p[1]

        pathBoard[x][y] = c
        count += 1

        n, pos = neighbors(x, y, pathBoard)
        for n, p in zip(n, pos):
            if n == "." and p != None:
                q.append(p)
    return count
        

pathBoard.insert(0, ["."] * 3 * len(board[0]))
color(0, 0, "O")
pathBoard = pathBoard[1:]

inside = 0
for x in range(0, len(pathBoard), 3):
    row = []
    for y in range(0, len(pathBoard[x]), 3):
        if pathBoard[x][y] == ".":
            inside += 1

print(inside)
assert 595 == inside

