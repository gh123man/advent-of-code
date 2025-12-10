# /// script
# dependencies = [
#   "shapely",
# ]
# ///

from shapely.geometry import Polygon, box
import itertools

f = open('input.txt', 'r')
coords = [x.split(",") for x in f.read().splitlines()]
coords = [(int(x[0]), int(x[1])) for x in coords]

areas = []
for c, q in itertools.combinations(coords, 2):
    areas.append(((abs(c[0] - q[0]) + 1) * (abs(c[1] - q[1]) + 1), c, q))

areas.sort()
print(areas[-1][0])

poly = Polygon(coords)
for v in areas[::-1]:
    shape = Polygon([v[1], (v[2][0], v[1][1]), v[2], (v[1][0], v[2][1])])
    if poly.contains(shape):
        print(v[0])
        break



