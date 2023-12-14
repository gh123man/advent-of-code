#!/opt/homebrew/bin/python3

f = open('14.txt', 'r')
lines = f.read().splitlines()

board = [list(line) for line in lines]

def transpose(m):
    m_reversed = m[::-1]
    return [[m_reversed[j][i] for j in range(len(m_reversed))] for i in range(len(m_reversed[0]))]

def run(board):
    for x, line in enumerate(board[1:]):
        x = x + 1
        for y, c in enumerate(line):
            if c == "O":
                i = 0
                while x - (i + 1) >= 0 and board[x - (i + 1)][y] == ".":
                    board[x - (i + 1)][y] = "O"
                    board[x - i][y] = "."
                    i += 1
    return board

def b2s(board):
    return "".join(["".join(line) for line in board])

last = ""
seenSet = {}

i = 0
# n = 1 # part 1
n = 4 * 1000000000 # part 2
while i < n:
    board = run(board)
    last = b2s(board)

    if last not in seenSet:
        seenSet[last] = i
    else:
        lastSeen = seenSet[last]
        offset = i - lastSeen

        remainder = n - i
        skipAmt = int(remainder / offset)
        if skipAmt > 0 and i + offset * skipAmt < n:
            i += offset * skipAmt
    if n != 1:
        board = transpose(board)
    i += 1


score = 0
for i, line in enumerate(board):
    for c in line:
        if c == "O":
            score += (len(board) - i)


print(score)
