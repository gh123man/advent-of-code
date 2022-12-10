#!/opt/homebrew/bin/python3
from collections import defaultdict

f = open('10.txt', 'r')

pc = 0

rom = []

for line in f.read().splitlines():
    split = line.split(" ")
    raw = split[0]

    if raw == "noop":
        rom.append(("noop"))
        continue

    reg = raw[len(raw) - 1]
    inst = raw[:-1]
    val = int(split[1])

    rom.append((inst, reg, val))
total = 0

m = defaultdict(lambda:1)
fp = 0
sub = 0
for pc in range(1, len(rom) * 3):
    p = "."

    sprint = m['x'] + 1
    if pc % 40 in [sprint -1, sprint, sprint +1]:
        p = "#"

    print(p, end = "")
    if pc % 40 == 0:
        print()

    if pc in [20, 60, 100, 140, 180, 220]:
        total += pc * m["x"]


    if fp == len(rom):
        break
    inst = rom[fp]
    if inst == "noop":
        fp += 1
        continue

    if inst[0] == "add":
        if sub < 1:
            sub += 1
            continue
        m[inst[1]] += inst[2]
        sub = 0
        fp += 1

print(total)
