#!/opt/homebrew/bin/python3

f = open('8.txt', 'r')

part1 = 0
part2 = 0

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
table2 = {}

def work(dir):
    for x in grid:
        cur = 0

        runlen = 0
        last = {}
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

            if y["val"] <= last["val"]:
                runlen += 1
                last = y
            else:
                print(runlen)
                table2[last["cord"]] = runlen
                runlen = 0


ans = {}
best = 0
for x, l in enumerate(grid2):
    endx = len(grid2)
    for y, v in enumerate(l):
        v = int(v)
        # DEBUG
        # x = 3
        # y = 2
        # l = grid2[x]
        # v = int(grid2[x][y])

        endy = len(l) 
        vd = 1

        if y == 0:
            continue
        if x == 0:
            continue

        print("start", x, y, v)
        av = 0
        for a in range(y+1, endy):
            av += 1
            if int(l[a]) >= v:
                break
        
        print("right", av)
        vd *= av 

        print()
        if y > 0 and y < len(l)-1:
            av = 0
            for a in range(y-1, -1, -1):
                av += 1
                print(a)
                if int(l[a]) >= v:
                    break
            print("left", av)
            vd *= av 


        av = 0
        for a in range(x+1, endx):
            n = int(grid2[a][y])
            av += 1
            if n >= v:
                break
        print(av)
        vd *= av 


        if x > 0 and x < len(grid2) - 1:
            av = 0
            for a in range(x-1, -1, -1):
                n = int(grid2[a][y])
                av += 1
                if n >= v:
                    break
            print(av)
            vd *= av 

        if vd > best:
            print("win", vd)
            best = vd




        
print(best)


# work(0)
# grid = list(zip(*grid[::-1]))
# work(1)
# grid = list(zip(*grid[::-1]))
# work(2)
# grid = list(zip(*grid[::-1]))
# work(3)


# print(len(table))
# print(table2)

# max = 0
# cords = ''
# for k, v in table:
#     if v > max:
#         max = v
#         cords = k

# print(table2)
# print(table)


# print(grid)
# print(table)
#rot = list(zip(*initial[::-1]))




