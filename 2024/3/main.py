#!/opt/homebrew/bin/python3 
import re

f = open('input.txt', 'r')
lines = f.read().splitlines()

p1 = 0
p2 = 0
do = True 
for line in lines:
    matches = [match.groups() for match in re.finditer(r'(mul\((\d\d*\d*)\,(\d\d*\d*)\))|(do\(\))|(don\'t\(\))', line)]
    for m in matches:
        if m[4] != None: 
            do = False
        elif m[3] != None:
            do = True
        elif m[0] != None:
            p1 += int(m[1]) * int(m[2])
            if do:
                p2 += int(m[1]) * int(m[2])
print(p1)
print(p2)