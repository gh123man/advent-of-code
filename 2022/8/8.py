#!/opt/homebrew/bin/python3

f = open('8.txt', 'r')

grid = []
grid2 = []

y = 0
for line in f.read().splitlines():
    x = 0
    grid.append([])
    grid2.append([])
    for c in line:
        grid2[y] = line
        grid[y].append({"cord": (x, y), "val": c})
        x += 1
    y += 1

table = {}
def work(dir):
    for x in grid:
        cur = 0

        for j, y in enumerate(x):
            if j == 0:
                cur = int(y["val"])
                table[y["cord"]] = y["val"]
                last = y
                continue
            if int(y["val"]) > cur:
                cur = int(y["val"])
                table[y["cord"]] = y["val"]
                continue 

for i in range(4):
    work(i)
    grid = list(zip(*grid[::-1]))

print(len(table))

best = 0
for x, l in enumerate(grid2):
    endx = len(grid2)
    for y, v in enumerate(l):
        v = int(v)
        endy = len(l) 
        vd = 1

        av = 0
        for a in range(y+1, endy):
            av += 1
            if int(l[a]) >= v:
                break
        vd *= av 

        if y > 0 and y < len(l)-1:
            av = 0
            for a in range(y-1, -1, -1):
                av += 1
                if int(l[a]) >= v:
                    break
            vd *= av 

        av = 0
        for a in range(x+1, endx):
            n = int(grid2[a][y])
            av += 1
            if n >= v:
                break
        vd *= av 

        if x > 0 and x < len(grid2) - 1:
            av = 0
            for a in range(x-1, -1, -1):
                n = int(grid2[a][y])
                av += 1
                if n >= v:
                    break
            vd *= av 

        if vd > best:
            best = vd

print(best)