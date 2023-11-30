f = open('3.txt', 'r')

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
i = 0
table = {}
for l in letters:
    i += 1
    table[l] = i
    
score = 0
score2 = 0

group = []
for line in f.read().splitlines():
    first = set(line[:int(len(line)/2)])
    second = set(line[int(len(line)/2):])
    score += table[first.intersection(second).pop()]

    group.append(line)
    if len(group) == 3:
        a = set(group[0])
        b = set(group[1])
        c = set(group[2])
        score2 += table[a.intersection(b).intersection(c).pop()]
        group = []

print(score)
print(score2)