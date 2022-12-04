f = open('4.txt', 'r')

sum = 0
part2 = 0
for line in f.read().splitlines():
    r = line.split(",")
    a1 = int(r[0].split("-")[0])
    a2 = int(r[0].split("-")[1])
    b1 = int(r[1].split("-")[0])
    b2 = int(r[1].split("-")[1])

    r1 = range(a1, a2)
    r1b = range(a1, a2 + 1)
    r2 = range(b1, b2)
    r2b = range(b1, b2 + 1)

    if (len(r1) == 0):
        sum += 1 if a1 in r2b else 0
        part2 += 1 if a1 in r2b else 0
    elif (len(r2) == 0):
        sum += 1 if b1 in r1b else 0
        part2 += 1 if b1 in r1b else 0
    else:
        sum += set((r1)).issubset(r2) or set((r2)).issubset(r1)
        part2 += len(set(r1b).intersection(r2b)) > 0
        
print(sum)
print(part2)