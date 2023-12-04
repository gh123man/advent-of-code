#!/opt/homebrew/bin/python3

f = open('4.txt', 'r')
lines = f.read().splitlines()

sum1 = 0
cardCount = [1] * len(lines)

for line in lines:
    originalCard = int(line.split(":")[0].split()[1])
    lists = line.split(":")[1]
    l1 = lists.split("|")[0]
    l2 = lists.split("|")[1]

    winning = set(l1.split())
    my = set(l2.split())

    mywin = len(winning & my)
    sum1 += 2 ** (mywin - 1) if mywin > 0 else 0

    if mywin > 0:
        for card in range(originalCard, min(originalCard + int(mywin), len(lines))): 
            cardCount[card] += cardCount[originalCard - 1]

print(sum1)
print(sum(cardCount))

