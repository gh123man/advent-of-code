#!/opt/homebrew/bin/python3
import itertools
from functools import cache


f = open('12.txt', 'r')
lines = f.read().splitlines()

def tokenize(problems):
    tokens = []
    last = ""
    buf = ""
    for c in problems:
        if c != last and buf != "":
            tokens.append(buf)
            buf = ""
        buf += c
        last = c
    if buf != "":
        tokens.append(buf)
    return tokens

def isSpring(token):
    return token[0] == "#"

def springs(tokens):
    return [t for t in tokens if t[0] == "#"]

def isValid(problem, constraints):
    tokens = tokenize(problem)
    for token in tokens:
        if isSpring(token):
            if len(constraints) == 0: 
                return False
            if len(token) != constraints[0]:
                return False
            else:
                if len(constraints) > 0:
                    constraints.pop(0)
                else:
                    return False
    if len(constraints) > 0:
        return False
    return True

def permute(token):
    return ["".join(p) for p in itertools.product(["#", "."], repeat=len(token))]

def expand(permutations):
    if len(permutations) == 1:
        return permutations[0]
    out = []
    for p in permutations[0]:
        for ex in expand(permutations[1:]):
            out.append(p + ex)
    return out


def exp1(t):
    k = []
    for a in t:
        if a[0] == "?":
            k.append(permute(a))
        else:
            k.append([a])
    return k

sum = 0
for line in lines:
    problem, constraint = line.split()
    constraint = [int(x) for x in constraint.split(",")]

    problem = exp1(tokenize(problem))

    for v in expand(problem):
        if isValid(v, constraint.copy()):
            sum += 1
print(sum)

assert 7260 == sum