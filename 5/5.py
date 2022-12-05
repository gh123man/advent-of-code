#!/opt/homebrew/bin/python3

f = open('5.txt', 'r')

part1 = 0
part2 = 0

initial = []
stacks = []
stacks2 = []


def makeStacks(initial):
    rot = list(zip(*initial[::-1]))
    stacks = []
    index = -1
    for i in rot:
        for c in i:
            if c.isdigit():
                stacks.append([])
                index += 1
                continue 
            if c.isalnum():
                stacks[index].append(c)
    return stacks

for line in f.read().splitlines():
    if len(line) == 0:
        stacks = makeStacks(initial)
        stacks2 = makeStacks(initial)
        continue

    if len(stacks) == 0:
        initial.append(line)
    else:
        ammount = int(line.split(" ")[1])
        fromStack = int(line.split(" ")[3])
        to = int(line.split(" ")[5])

        for i in range(0, ammount):
            stacks[to - 1].append(stacks[fromStack - 1].pop())

        stacks2[to - 1] += stacks2[fromStack - 1][-(ammount):]
        stacks2[fromStack - 1] = stacks2[fromStack - 1][:-ammount]


for s in stacks:
    print(s.pop(), end = "")

print()
for s in stacks2:
    print(s.pop(), end = "")

print()





#print(rot)
#print(part1)
#print(part2)