
f = open('1.txt', 'r')

top = [0, 0, 0]
curr = 0
for line in f.read().splitlines() :
    if line.isnumeric():
        curr += int(line)
        continue
    if curr > top[0]: 
        top[0] = curr
        top.sort()
        print(top)
    
    curr = 0

print(sum(top))