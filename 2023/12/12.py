#!/opt/homebrew/bin/python3
from functools import cache

f = open('12.txt', 'r')
lines = f.read().splitlines()

def topSpring(springs):
    if springs == "":
        return 0
    return [int(x) for x in springs.split(",")][0]

def dropSpring(springs):
    if springs == "":
        return ""
    sprs = [int(x) for x in springs.split(",")]
    if sprs[0] == 0:
        return ",".join([str(s) for s in sprs[1:]])
    sprs[0] -= 1
    return ",".join([str(s) for s in sprs])

@cache
def solveRec(input, springs):
    if len(input) == 0:
        if springs == "0":
            return 1
        return 0

    combos = 0
    c = input[0]
    input = input[1:]
    ts = topSpring(springs)

    if (c == "." or c == "?") and ts == 0:
        combos += solveRec(input, dropSpring(springs))
        combos += solveRec(input, springs)

    if c == "#" and ts != 0:
        combos += solveRec(input, dropSpring(springs))

    if c == "?" and ts != 0:
        combos += solveRec(input, dropSpring(springs))

    return combos

def solve(input, springs):
    return solveRec("." + input, "0," + springs)

sum = 0
for line in lines:
    prob, const = line.split()
    prob = "?".join([prob] * 5) # part 2
    const = ",".join([const] * 5) # part 2
    sum += solve(prob, const)


print(sum)