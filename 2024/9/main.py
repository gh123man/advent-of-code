#!/opt/homebrew/bin/python3 
from re import A

f = open('input.txt', 'r')
line = f.read().splitlines()

grid = []
buf = []
useSize = True
blockId = 0
for i, c in enumerate(line[0]):
    if useSize:
        for n in range(int(c)):
            buf.append(str(blockId))
        useSize = False
        blockId += 1
    else:
        for n in range(int(c)):
            buf.append(".")
        useSize = True

startPtr = 0
part1 = buf.copy()
part2 = buf.copy()
while startPtr < len(part1):
    while startPtr < len(part1) and part1[startPtr] != ".":
        startPtr += 1
    if startPtr == len(part1):
        break
    c = part1.pop()
    part1[startPtr] = c
    
def checksum(buf):
    sum = 0
    for i, c in enumerate(buf):
        if c == ".":
            continue
        sum += int(c) * i
    return sum

def getBlock(buffer):
    start = len(buffer) - 1
    end = start
    while buffer[end] == ".":
        end -= 1
        start -= 1
    while buffer[end] == buffer[start]:
       start -= 1
    return (start+1, end+1)


def seekSpan(buffer, count):
    i = 0
    while i < len(buffer) and buffer[i] != ".":
        i += 1
        if i >= len(buffer):
            return -1
        span = 0
        while i + span < len(buffer) and buffer[i + span] == ".":
            span += 1
        if span >= count:
            return i
        i += span
    return -1

backset = len(part2)
tail = []
while len(part2[:backset]) > 2:
    (bs, be) = getBlock(part2[:backset])
    idx = seekSpan(part2[:backset], be - bs)
    backset = bs
    if idx == -1 or idx > bs:
        continue
    part2 = part2[:idx] + part2[bs:be] + part2[idx + (be-bs):bs] + ["." for _ in range(be - bs)] + part2[be:]
    tail = []


print(''.join(part2))
print(checksum(part1))
print(checksum(part2))





