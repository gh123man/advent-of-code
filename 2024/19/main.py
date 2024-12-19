from lib import *
from functools import cache

lines = lines("input.txt")

parts = tuple(lines[0].split(", "))
designs = lines[2:]

@cache
def possible(design, parts):
    if design == "":
        return 1
    paths = 0
    for part in parts:
        if design.startswith(part):
            paths += possible(design.removeprefix(part), parts)
    return paths
    
sum = 0
paths = 0
for design in designs:
    p = possible(design, parts) 
    paths += p
    if p > 0:
        sum += 1
print(sum, paths)