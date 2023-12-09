#!/opt/homebrew/bin/python3

from functools import cmp_to_key

f = open('7.txt', 'r')

cards1 = "AKQJT98765432"[::-1]
cards2 = "AKQT98765432J"[::-1]
deck = []
lines = f.read().splitlines()
for line in lines:
    deck.append((line.split()[0], int(line.split()[1])))

def score(card, p2):
    d = {}
    for c in card:
        if c not in d:
            d[c] = 0
        d[c] += 1

    j = 0
    if "J" in d and p2:
        j = d["J"]
        del d["J"]
        if j == 5:
            return 7
        
    raw = max(d.values()) + j
    if raw > 3: # 5, 4
        return raw + 2
    if raw == 3:
        if len(d) == 2:
            return 5 # Full house
        if len(d) == 3:
            return 4 # 3 of a kind

    if raw == 2:
        c = 0
        for v in d.values():
            if v == raw:
                c += 1
        if c == 2:
            return 3 # 2 pair
        return 2 # 1 pair
    return 1

def score2(carda, cardb, cards):
    for a, b in zip([cards.index(x) for x in carda], [cards.index(x) for x in cardb]):
        if a > b:
            return -1
        if b > a:
            return 1
    return 0

def mkSort(p2):
    def sortfn(a, b):
        sa = score(a[0], p2)
        sb = score(b[0], p2)
        if sa == sb:
            return score2(a[0], b[0], cards2 if p2 else cards1)
        else:
            return sb - sa
    return sortfn
    
def sortfnP2(a, b):
    sa = score(a[0])
    sb = score(b[0])
    if sa == sb:
        return score2(a[0], b[0], cards2)
    else:
        return sb - sa


deck1 = sorted(deck, key=cmp_to_key(mkSort(False)))
p1 = sum([x[1] * (i + 1) for i, x in enumerate(deck1[::-1])])
print(p1)


deck2 = sorted(deck, key=cmp_to_key(mkSort(True)))
p2 = sum([x[1] * (i + 1) for i, x in enumerate(deck2[::-1])])
print(p2)