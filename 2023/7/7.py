#!/opt/homebrew/bin/python3


         # 253581847
# too high 253628670
         # 253494910
         # 247497408
         # 253921968
         # 255145847
         # 252206616
         # 246240998
         # 246940538
         # 248172902

from functools import cmp_to_key

f = open('7.txt', 'r')

cards = "AKQJT98765432"[::-1]
deck = []
lines = f.read().splitlines()
for line in lines:
    deck.append((line.split()[0], int(line.split()[1])))

def score(card):
    d = {}
    for c in card:
        if c not in d:
            d[c] = 0
        d[c] += 1
    raw = max(d.values())
    highCard = max([cards.index(x) for x in card])
    if raw > 3: # 5, 4
        return (raw + 2, 0)
    if raw == 3:
        if len(d) == 2:
            return (5, 0) # Full house
        if len(d) == 3:
            return (4, 0) # 3 of a kind

    if raw == 2:
        c = 0
        for v in d.values():
            if v == raw:
                c += 1
        if c == 2:
            return (3, 0) # 2 pair
        return (2, 0) # 1 pair
    return (1, highCard)
    

def score2(carda, cardb):
    for a, b in zip([cards.index(x) for x in carda], [cards.index(x) for x in cardb]):
        print(a, b)
        if a > b:
            return -1
        if b > a:
            return 1 #  ???
    return 0

def sortfn(a, b):
    sa, saa = score(a[0])
    sb, sbb = score(b[0])
    print(a[0], b[0], sa, sb, saa, sbb)
    if sa == sb:
        if sa == 1:
            return sbb - saa
        # print("h")
        return score2(a[0], b[0])
    else:
        return sb - sa


deck = sorted(deck, key=cmp_to_key(sortfn))

result = sum([x[1] * (i + 1) for i, x in enumerate(deck[::-1])])
for i, x in enumerate(deck[::-1]):
    print(x[0], x[1])



# print(deck)
print(result)
