#!/opt/homebrew/bin/python3

f = open('9.txt', 'r')

seq = []
lines = f.read().splitlines()
for line in lines:
    seq.append([[int(x) for x in line.split()]])

p1 = 0
p2 = 0
for s in seq:
    inset = 1
    while sum([abs(x) for x in s[-1]]) != 0:
        lst = s[-1]
        buf = [0] * len(lst)
        for i in range(inset, len(lst)):
            buf[i] = lst[i] - lst[i - 1]
        inset += 1 
        s.append(buf)

    s[-1].append(0)

    for i in range(len(s)-1, 0, -1):
        s[i - 1].append(s[i - 1][-1] + s[i][-1])
    p1 += s[0][-1]

    for i in range(len(s)-1, 0, -1):
        s[i - 1].insert(0, 0)
        s[i - 1][i - 1] = (s[i - 1][i] - s[i][i])
    p2 += s[0][0]


print(p1)
print(p2)
