#!/opt/homebrew/bin/python3

from lib import *

f = open('input.txt', 'r')
lines = f.read().splitlines()

ranges = []
items = []
fillItems = False
for line in lines:
    if line == "":
        fillItems = True
        continue
    if fillItems:
        items.append(int(line))
        continue
    ranges.append(range(int(line.split("-")[0]), int(line.split("-")[1]) + 1))

part1 = 0
for item in items:
    for r in ranges:
        if item in r:
            part1 += 1
            break

compressedRanges = []
ranges.sort(key=lambda x: x.start)

while len(ranges) > 0:
    curRange = ranges.pop(0)
    toRemove = []
    for i, r in enumerate(ranges):
        if r.start in curRange:
            curRange = range(curRange.start, max(curRange.stop, r.stop))
            toRemove.append(i)
    for i in toRemove[::-1]:
        ranges.pop(i)
    compressedRanges.append(curRange)

print(sum([len(r) for r in compressedRanges]))