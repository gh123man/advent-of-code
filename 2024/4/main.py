#!/opt/homebrew/bin/python3 
import re

f = open('input.txt', 'r')
lines = f.read().splitlines()
directions = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]

grid = []
for line in lines:
    grid.append(list(line))

def getRope(direction, grid, row, col, maxLen):
    rope = ""
    while len(rope) < maxLen:
        row += direction[0]
        col += direction[1]
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
            break
        char = grid[row][col]
        rope += char
    return rope

def isXMas(grid, row, col):
    middle = grid[row][col]
    a = getRope((-1, -1), grid, row, col, 1) + middle + getRope((1, 1), grid, row, col, 1)
    b = getRope((-1, 1), grid, row, col, 1) + middle + getRope((1, -1), grid, row, col, 1)
    if (a == "SAM" or a == "MAS") and (b == "SAM" or b == "MAS"):
        return True
    return False
    

count = 0
count2 = 0
for row in range(len(grid)):
    for col in range(len(grid[row])):
        char = grid[row][col]
        if char == "X":
            for d in directions:
                rope = "X" + getRope(d, grid, row, col, 3)
                if rope == "XMAS":
                    count += 1
        if char == "A" and isXMas(grid, row, col):
            count2 += 1

print(count)
print(count2)