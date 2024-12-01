#!/opt/homebrew/bin/python3

from collections import defaultdict

f = open('input.txt', 'r')
lines = f.read().splitlines()

left, right = [], []
for line in lines:
    d = line.split()
    left.append(int(d[0]))
    right.append(int(d[1]))

left.sort()
right.sort()

sum = 0
index = defaultdict(int)
for x in zip(left, right):
    sum += abs(x[0] - x[1])
    index[x[1]] += 1

p2sum = 0
for v in left:
    p2sum += v * index[v]

# Part 1
print(sum)
# Part 2
print(p2sum)

