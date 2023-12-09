#!/opt/homebrew/bin/python3

import math 

f = open('8.txt', 'r')
lines = f.read().splitlines()

inst = lines[0]
graph = {}
for i in range(2, len(lines)):
    k = lines[i].split(" = ")[0]
    v = tuple(lines[i].split(" = ")[1][1:-1].split(", "))
    graph[k] = v


node = "AAA"

nodes = [k for k in graph.keys() if k [-1] == "A"]

def solve(node, p2):
    done = False
    step = 0
    while not done:
        for c in inst:
            step += 1
            if c == "L":
                node = graph[node][0]
            else:
                node = graph[node][1]
            if (p2 and node[-1] == "Z") or (not p2 and node == "ZZZ"):
                done = True
                break; 
    return step

res = 1
for n in nodes:
    res = math.lcm(res, solve(n, True))

print(solve(node, False)) # part 1
print(res) # part 2

        