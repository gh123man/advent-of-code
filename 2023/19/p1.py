#!/opt/homebrew/bin/python3
import json

f = open('19.txt', 'r')
lines = f.read().splitlines()

ops = {
    ">": lambda x, y: x > y,
    "<": lambda x, y: x < y,
}

def buildRule(rules):
    processors = []
    for r in rules:
        if len(r.split(":")) == 1:
            processors.append(lambda _: r)
        else:
            rhs, dest = r.split(":")
            var, op, comp = "", "", ""
            if len(rhs.split(">")) > 1:
                var, comp = rhs.split(">")
                op = ">"
            else:
                var, comp = rhs.split("<")
                op = "<"
            def retCpy(var=var, op=op, comp=comp, dest=dest):
                return lambda part: dest if ops[op](part[var], int(comp)) else None
            processors.append(retCpy())
    return processors


workflows = {}
parts = []
procWorkflows = True
for line in lines:
    if line == "":
        procWorkflows = False
        continue
        
    if procWorkflows:
        name = line.split('{')[0]
        wf = line.split('{')[1][:-1]
        rules = wf.split(',')
        workflows[name] = buildRule(rules)
    else:
        obj = {}
        for k in line[1:][:-1].split(','):
            obj[k.split('=')[0]] = int(k.split('=')[1])
        parts.append(obj)

accepted = []

def executeWorkflow(part, workflow):
    for processor in workflow:
        dest = processor(part)
        if dest != None:
            return dest
    return None
    
for part in parts:
    dest = "in"
    while dest != "A" and dest != "R":
        dest = executeWorkflow(part, workflows[dest])
    if dest == "A":
        accepted.append(part)

s = 0
for p in accepted: 
    for v in p.values():
        s += v
print(s)
    
