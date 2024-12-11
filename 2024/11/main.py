#!/opt/homebrew/bin/python3 
from functools import cache

f = open('input.txt', 'r')
line = [int(x) for x in f.read().splitlines()[0].split()]

@cache
def process(stone, depth):
    if depth == 0:
        return 1 
    
    if stone == 0:
        return process(1, depth - 1)
    
    strstone = str(stone)
    if len(strstone) % 2 == 0:
        return process(int(strstone[:len(strstone)//2]), depth - 1) + process(int(strstone[len(strstone)//2:]), depth - 1)

    return process(stone * 2024, depth - 1)


def getScore(depth):
    sum = 0
    for stone in line:
        sum += process(stone, depth)
    return sum

print(getScore(25))
print(getScore(75))


