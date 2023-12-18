import numpy as np

f = open('18.txt', 'r')
lines = f.read().splitlines()
dirs = { "U": (-1, 0), "R": (0, 1), "D": (1, 0), "L": (0, -1)}
dirs2 = { 3: (-1, 0), 0: (0, 1), 1: (1, 0), 2: (0, -1)}

def solve(part2):
    points = [(0, 0)]
    perim = 0
    pos = (0, 0)

    for line in lines:
        dir = line.split()[0]
        leng = int(line.split()[1])

        # part 2
        if part2:
            dir = int(line.split("#")[1][:-1][-1])
            leng = int(line.split("#")[1][:-2], 16)
            pos = (pos[0] + (dirs2[dir][0] * leng), pos[1] + (dirs2[dir][1] * leng))
        else:
            pos = (pos[0] + (dirs[dir][0] * leng), pos[1] + (dirs[dir][1] * leng))

        perim += leng
        points.append(pos)

    x, y = zip(*points)
    return x, y, perim

# Stolen from https://stackoverflow.com/a/30408825/1152375
def PolyArea(x,y):
    return 0.5*np.abs(np.dot(x,np.roll(y,1))-np.dot(y,np.roll(x,1)))

x, y, perim = solve(False)
print(int(PolyArea(x, y) + (perim / 2) + 1))
x, y, perim = solve(True)
print(int(PolyArea(x, y) + (perim / 2) + 1))
