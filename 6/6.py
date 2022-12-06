#!/opt/homebrew/bin/python3

f = open('6.txt', 'r')

# 4 vs 14 for part 1 vs part 2
part1 = 0

queue = []
for line in f.read().splitlines():
    i = 0
    for c in line:
        i += 1
        queue.insert(0, c)
        if len(queue) == 14:
            s = set(queue)
            if len(s) == 14:
                part1 = i
                break
            queue.pop()


print(part1)