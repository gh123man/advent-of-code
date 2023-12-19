#!/opt/homebrew/bin/python3
import json

f = open('19.txt', 'r')
lines = f.read().splitlines()

def buildRule(rules):
    processors = []
    for r in rules:
        if len(r.split(":")) == 1:
            processors.append((r,))
        else:
            rhs, dest = r.split(":")
            var, op, comp = "", "", ""
            if len(rhs.split(">")) > 1:
                var, comp = rhs.split(">")
                op = ">"
            else:
                var, comp = rhs.split("<")
                op = "<"
            processors.append((var, op, int(comp), dest))
    return processors


workflows = {}
for line in lines:
    if line == "":
        break
    name = line.split('{')[0]
    wf = line.split('{')[1][:-1]
    rules = wf.split(',')
    workflows[name] = buildRule(rules)

accepted = []
q = [("in", {"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)})]

while q:
    dest, obj = q.pop(0)
    if dest == "R": continue
    if dest == "A":
        accepted.append(obj)
        continue

    steps = workflows[dest]
    for step in steps:
        if len(step) == 1:
            q.append((step[0], obj))
            break

        var, op, comp, d = step
        l, r = obj[var]

        if l >= comp >= r: continue
        cpy = obj.copy()

        if op == ">":
            obj[var] = (l, comp)
            cpy[var] = (comp + 1, r)
        else:
            cpy[var] = (l, comp - 1)
            obj[var] = (comp, r)
        q.append((d, cpy))
    

part2 = 0
for a in accepted:
    s = 1
    for v in a.values():
        s *= (v[1] - v[0] + 1)
    part2 += s
print(part2)