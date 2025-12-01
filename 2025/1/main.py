#!/opt/homebrew/bin/python3

from collections import defaultdict

f = open('input.txt', 'r')
lines = f.read().splitlines()

part1 = 0
part2 = 0 
dial = 50
for line in lines:
    direction = line[0]
    amount = int(line[1:])

    if direction == "L":
        for i in range(amount):
            dial -= 1
            if dial == 0:
                part2 += 1
            if dial < 0:
                dial = 99
    else:
        for i in range(amount):
            dial += 1
            if dial == 100:
                part2 += 1
                dial = 0
    if dial == 0:
        part1 += 1

print(part1)
print(part2)