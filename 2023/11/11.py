#!/opt/homebrew/bin/python3

f = open('11.txt', 'r')
lines = f.read().splitlines()
board = []
galaxies = []
offset = 0
 
# part 2, change to 1 for part 1
expand = 1000000 - 1
rowsAdded = 0
for x, line in enumerate(lines):
    dot = 0
    row = []
    for y, c in enumerate(line):
        if c == '.':
            dot += 1
            row.append(".")
        else:
            row.append((x + (rowsAdded * expand), y))
    board.append(row)
    if dot == len(line):
        rowsAdded += 1

colsAdded = 0
for y in range(len(board[0])):
    dot = 0
    for x in range(len(board)):
        if board[x][y] == ".":
            dot += 1
        else:
            galaxies.append((board[x][y][0], board[x][y][1] + (colsAdded * expand)))
    if dot == len(board):
        colsAdded += 1

for x, line in enumerate(board):
    for y, c in enumerate(line):
        if c == "#":
            galaxies.append((x, y))

sum = 0
pair = 0
seen = set()
for a in galaxies:
    for b in galaxies:
        key = tuple(sorted([a, b]))
        if a != b and key not in seen:
            pair += 1
            res = abs(a[0] - b[0]) + abs(a[1] - b[1])
            sum += res 
            seen.add(key)

print(sum)
