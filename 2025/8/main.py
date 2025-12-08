#!/opt/homebrew/bin/python3

from lib import *
from math import sqrt

f = open('input.txt', 'r')
points = [tuple(map(int, x.split(','))) for x in f.read().splitlines()]

def euclideanDistance(p1, p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)

distances = []
seen = set()

for p in points:
    for q in points:
        if p == q:
            continue
        if (p, q) in seen or (q, p) in seen:
            continue
        seen.add((p, q))
        distances.append((euclideanDistance(p, q), p, q))

distances.sort()
sets = []
part2 = False
for i, d in enumerate(distances):
    found_sets = [s for s in sets if d[1] in s or d[2] in s]
    
    populated = len(sets) > 1
    if len(found_sets) == 0:
        sets.append(set([d[1], d[2]]))
    elif len(found_sets) == 1:
        found_sets[0].add(d[1])
        found_sets[0].add(d[2])
    else:
        merged = found_sets[0].union(*found_sets[1:])
        merged.add(d[1])
        merged.add(d[2])
        for s in found_sets:
            sets.remove(s)
        sets.append(merged)

    if not part2 and len(sets) == 1 and sets[0] == set(points):
        print("part 2:", d[1][0] * d[2][0])
        part2 = True


    if i == 999:
        sets.sort(key=lambda x: len(x), reverse=True)
        total = 1
        for s in sets[:3]:
            total *= len(s)
        print("part 1:", total)
