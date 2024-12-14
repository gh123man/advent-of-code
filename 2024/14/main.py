#!/opt/homebrew/bin/python3 
import re

f = open('input.txt', 'r')
lines = f.read().splitlines()
pattern = re.compile(r"p=(\d+),(\d+)\sv=(-?\d+),(-?\d+)")

class Vec:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, vec):
        return Vec(self.x + vec.x, self.y + vec.y)

class Drone:
    def __init__(self, board, pos, direction):
        self.board = board
        self.pos = pos
        self.direction = direction

    def move(self):
        self.pos.x =  (self.pos.x + self.direction.x) % self.board.x
        self.pos.y =  (self.pos.y + self.direction.y) % self.board.y

class Quad:
    def __init__(self, point, size):
        self.point = point
        self.size = size
    
    def contains(self, point):
        return point.x >= self.point.x and point.x < self.size.x and point.y >= self.point.y and point.y < self.size.y
    
def draw(drones):
    board = drones[0].board
    for y in range(board.y):
        for x in range(board.x):
            count = 0
            for d in drones:
                if d.pos.x == x and d.pos.y == y:
                    count += 1
            if count > 0:
                print(count, end="")
            else:
                print(" ", end="")
        print()

drones = []
board = Vec(101, 103)

for line in lines:
    match = pattern.search(line)
    px, py, dx, dy = (int(match.group(1)), int(match.group(2)), int(match.group(3)), int(match.group(4)))
    drones.append(Drone(board, Vec(px, py), Vec(dx, dy)))

dx = Vec(board.x // 2, 0)
dy = Vec(0, board.y // 2)
x1 = Vec(1, 0)
y1 = Vec(0, 1)
origin = Vec(0, 0)

q1 = Quad(origin, origin.add(dx).add(dy))
q2 = Quad(dx.add(x1), q1.size.add(dx).add(x1))
q3 = Quad(dy.add(y1), q1.size.add(dy).add(y1))
q4 = Quad(dy.add(dx).add(x1).add(y1), origin.add(dx).add(dy).add(dx).add(dy).add(x1).add(y1))

quads = [q1, q2, q3, q4]
i = 0

# Part 1
for i in range(0, 100):
    for d in drones:
        d.move()
    i += 1

total = 1
for q in quads:
    sum = 0
    for d in drones:
        if q.contains(d.pos):
            sum += 1
    total *= sum
print(total)

# part 2
a = 7892 # I found it!
while True:
    for d in drones:
        d.move()
    i += 1
    if i == a:
        draw(drones)
        break
print(a)
