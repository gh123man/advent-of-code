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

def solve(nextPos, direction):
    drawBoard = [list(line) for line in board]
    q = [(nextPos, direction)] 
    term = set()

    while q:
        nextPos = (nextPos[0] + directions[direction][0], nextPos[1] + directions[direction][1])

        if nextPos in term or nextPos[0] < 0 or nextPos[0] >= len(board) or nextPos[1] < 0 or nextPos[1] >= len(board[0]):
            nextPos, direction = q.pop(0)
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
    s = 0
    for l in drawBoard:
        s += sum([1 for x in l if x == "#"])
    return s

# Part 1
drawBoard = solve((0, -1), 1)
print(score(drawBoard))

# Part 2
s = 0
for y in range(len(board[0])):
    s = max(score(solve((-1, y), 2)), s)
    s = max(score(solve((len(board), y), 0)), s)

for x in range(len(board)):
    s = max(score(solve((x, -1), 1)), s)
    s = max(score(solve((x, len(board[0])), 3)), s)

print(s)