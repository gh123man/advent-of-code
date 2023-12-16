#!/opt/homebrew/bin/python3

f = open('16.txt', 'r')
board = f.read().splitlines()

turns = "/\\"
upDirs    = " / \\"
downDirs  = " \\ /"
rightDirs = "/ \\ "
leftDirs  = "\\ / "
redirects = [upDirs, rightDirs, downDirs, leftDirs]
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def solve(start, dir):
    drawBoard = []
    for line in board:
        drawBoard.append(list(line))

    nextPos = start
    direction = dir
    q = [(nextPos, direction)] # Push moves onto queue
    term = set()
    while q:
        nextPos = (nextPos[0] + directions[direction][0], nextPos[1] + directions[direction][1])

        if nextPos in term or nextPos[0] < 0 or nextPos[0] >= len(board) or nextPos[1] < 0 or nextPos[1] >= len(board[0]):
            nextPos, direction = q.pop(0)

            if nextPos not in term:
                term.add(nextPos)
            continue
        drawBoard[nextPos[0]][nextPos[1]] = "#"
        next = board[nextPos[0]][nextPos[1]]

        if next == "|" and (direction == 1 or direction == 3):
            q.append((nextPos, 0))
            direction = 2

        if next == "-" and (direction == 0 or direction == 2):
            q.append((nextPos, 1))
            direction = 3

        if next in turns:
            direction = redirects[direction].index(next)

    return drawBoard

def score(drawBoard):
    sum = 0
    for l in drawBoard:
        for x in l:
            if x == "#":
                sum += 1
    return sum

# Part 1
drawBoard = solve((0, -1), 1)
s = score(drawBoard)
print(s)

# Part 2
s = 0
for y in range(len(board[0])):
    b = solve((-1, y), 2)
    s = max(score(b), s)

for y in range(len(board[0])):
    b = solve((len(board), y), 0)
    s = max(score(b), s)

for x in range(len(board)):
    b = solve((x, -1), 1)
    s = max(score(b), s)

for x in range(len(board)):
    b = solve((x, len(board[0])), 3)
    s = max(score(b), s)

print(s)