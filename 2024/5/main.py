#!/opt/homebrew/bin/python3 
import re

f = open('input.txt', 'r')
lines = f.read().splitlines()

rules = []
pages = []
parseLines = True
for line in lines:
    if line == "":
        parseLines = False
        continue

    if parseLines:
        rules.append(line.split("|"))
    else:
        pages.append(line.split(","))

def pageMatchesRule(rule, page):
    try:
        return page.index(rule[0]) < page.index(rule[1])
    except:
        return True
    
def shiftLeft(rule, page):
    while not pageMatchesRule(rule, page):
        idxA = page.index(rule[0])
        page[idxA], page[idxA-1] = page[idxA-1], page[idxA]
    return page
    

def pageMatchRules(rs, page):
    for r in rs:
        if not pageMatchesRule(r, page):
            return False
    return True

middles = []
middles2 = []
for page in pages: 
    match = True
    activeRules = []
    for r in rules:
        if set(r) <= set(page):
            activeRules.append(r)


    if pageMatchRules(activeRules, page):
        middles.append(int(page[int(len(page)/2)]))
    else:
        while not pageMatchRules(activeRules, page):
            for r in activeRules:
                if not pageMatchesRule(r, page):
                    page = shiftLeft(r, page)
        middles2.append(int(page[int(len(page)/2)]))


print(sum(middles))
print(sum(middles2))

