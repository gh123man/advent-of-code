#!/opt/homebrew/bin/python3

f = open('6.txt', 'r')
lines = f.read().splitlines()

races = [int(x) for x in lines[0].split()[1:]]
best = [int(x) for x in lines[1].split()[1:]]

def solve(races, best):
    tot = 1
    for i, r in enumerate(races):
        tot *= len([t for t in range(r) if ((r - t) * t) > best[i]])
    return tot

print(solve(races, best)) # Part 1

races = [int("".join(lines[0].split()[1:]))]
best = [int("".join(lines[1].split()[1:]))]

print(solve(races, best)) # Part2
