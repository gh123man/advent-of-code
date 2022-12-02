

f = open('2.txt', 'r')

## AX rock 1 
# BY paper 2
# CZ sicors 3

# win 6
# draw 3
# los 0

# x lose
# y draw
# z win

table2 = {
    "A X": "A Z",
    "A Y": "A X",
    "A Z": "A Y",
    "B X": "B X",
    "B Y": "B Y",
    "B Z": "B Z",
    "C X": "C Y",
    "C Y": "C Z",
    "C Z": "C X",
}
table = {
    "A X": 3 + 1,
    "A Y": 6 + 2,
    "A Z": 0 + 3,
    "B X": 0 + 1,
    "B Y": 3 + 2,
    "B Z": 6 + 3,
    "C X": 6 + 1,
    "C Y": 0 + 2,
    "C Z": 3 + 3,
}

part1 = 0
part2 = 0
for line in f.read().splitlines():
    part1 += int(table[line])
    part2 += int(table[table2[line]])
print(part1)
print(part2)