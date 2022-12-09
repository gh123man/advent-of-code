#!/opt/homebrew/bin/python3

f = open('9.txt', 'r')
pos = [0, 0]
tail = [0, 0]

def touching(a, b):
    return abs(a[0] - b[0]) <= 1 and abs(a[1] - b[1]) <= 1 

def touching2(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


poss = set()
poss2 = set()

chain = [[0,0] for _ in range(10)]
for line in f.read().splitlines():
    split = line.split(" ")
    dir = split[0]
    times = int(split[1])

    for i in range(times):
        last = pos.copy()
        clast = chain[0].copy()
        if dir == "R":
            pos[0] += 1
            chain[0][0] += 1
        if dir == "L":
            pos[0] -= 1
            chain[0][0] -= 1
        if dir == "U":
            pos[1] += 1
            chain[0][1] += 1
        if dir == "D":
            pos[1] -= 1
            chain[0][1] -= 1

        head = chain[0].copy()
        for i in range(len(chain)):
            if i == 0: 
                continue
            cur = chain[i]
            if not touching(head, cur):
                if touching2(head, cur) > 2:
                    if touching(head, [cur[0] + 1, cur[1] + 1]):
                        chain[i] = [cur[0] + 1, cur[1] + 1]
                    elif touching(head, [cur[0] - 1, cur[1] - 1]):
                        chain[i] = [cur[0] - 1, cur[1] - 1]
                    elif touching(head, [cur[0] + 1, cur[1] - 1]):
                        chain[i] = [cur[0] + 1, cur[1] - 1]
                    elif touching(head, [cur[0] - 1, cur[1] + 1]):
                        chain[i] = [cur[0] - 1, cur[1] + 1]
                elif touching2(head, cur) == 2:
                    if touching(head, [cur[0] + 1, cur[1]]):
                        chain[i] = [cur[0] + 1, cur[1]]
                    elif touching(head, [cur[0] - 1, cur[1]]):
                        chain[i] = [cur[0] - 1, cur[1]]
                    elif touching(head, [cur[0], cur[1] + 1]):
                        chain[i] = [cur[0], cur[1] + 1]
                    elif touching(head, [cur[0], cur[1] - 1]):
                        chain[i] = [cur[0], cur[1] - 1]
            head = chain[i].copy()
                
        poss2.add(str(chain[-1]))


        if not touching(pos, tail):
            tail = last
            poss.add(str(tail))

print(len(poss) + 1)
print(len(poss2))


