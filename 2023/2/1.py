#!/opt/homebrew/bin/python3

f = open('2.txt', 'r')

base = {
    "red": 0,
    "green": 0,
    "blue": 0,
}

part1 = 0
part2 = 0

for line in f.read().splitlines():
    sett = line.split(": ")[1].split(";")
    game = int(line.split(": ")[0].split(" ")[1])

    fail = False

    mins = {
        "red": 100000000000000,
        "green": 100000000000000,
        "blue": 100000000000000,
    }
    bag2 = base.copy()

    for s in sett:
        bag1 = {
            "red": 12,
            "green": 13,
            "blue": 14,
        }
        
        opts = s.split(",")
        bag2 = base.copy()
        for opt in opts:
            num, col = int(opt.strip().split(" ")[0].strip()), opt.strip().split(" ")[1]

            bag1[col] -= num
            bag2[col] -= num
            if bag1[col] < 0:
                fail = True
            if bag2[col] < mins[col]:
                mins[col] = bag2[col]

    if not fail:
        part1 += game
    part2 += int(base["red"] - mins["red"]) * (base["green"] - mins["green"]) * (base["blue"] - mins["blue"])

print(part1)
print(part2)