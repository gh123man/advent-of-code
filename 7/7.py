#!/opt/homebrew/bin/python3

f = open('7.txt', 'r')

part1 = 0
part2 = 0

context = {}
stack = []

for line in f.read().splitlines():
    parts = line.split(" ")

    if parts[0] == "$" and parts[1] == "cd" and parts[2] == "..":
        stack.pop()
        continue

    if parts[0] == "$" and parts[1] == "cd":
        stack.append(parts[2])
        context[str(stack)] = [0]
        continue
        

    if parts[0].isnumeric():
        context[str(stack)][0] += int(parts[0])
        continue

    if parts[0] == "dir":
        context[str(stack)].append(str(stack + [parts[1]]))
        continue

    
def resolve(key):
    sum = context[key][0]
    for k in context[key][1:]:
        if k != key:
            sum += resolve(k)
    return sum


sz = 70000000 - resolve("['/']")
candidates = []
for key in context.keys():
    if resolve(key) <= 100000:
        part1 += resolve(key)

    if resolve(key) > 30000000 - sz:
        candidates.append(resolve(key))


print(part1)
print(min(candidates))
