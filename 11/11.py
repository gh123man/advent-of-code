#!/opt/homebrew/bin/python3
from collections import defaultdict
import math

f = open('11.txt', 'r')

class Monkey:
    def __init__(self):
        self.items = []
        self.operation = ""
        self.test = ""
        self.true = ""
        self.false = ""
        self.inspected = 0
        pass

monkeys = []
derek = 1

cur = {}
for line in f.read().splitlines():
    splits = line.strip().split(" ")
    if splits[0] == "Monkey":
        monkeys.append(Monkey())
        cur = monkeys[-1]
        continue

    if splits[0] == "Starting":
        cur.items += [x.replace(",", "") for x in splits[2:]]
        continue

    if splits[0] == "Operation:":
        cur.operation = line.split("=")[1].strip()

    if splits[0] == "Test:":
        cur.test = int(splits[3])
        derek *= cur.test

    if splits[0] == "If" and splits[1] == "true:":
        cur.true = int(splits[5])

    if splits[0] == "If" and splits[1] == "false:":
        cur.false = int(splits[5])


def is_square(i) -> bool:
    return i == math.isqrt(i) ** 2

for i in range(10000):
    for monkey in monkeys:
        while len(monkey.items) > 0:
            monkey.inspected += 1
            item = monkey.items.pop()
            new = math.floor(eval(monkey.operation.replace("old", str(item))))
            new = (new % derek) + derek

            if new % monkey.test == 0:
                monkeys[monkey.true].items.append(new)
            else:
                monkeys[monkey.false].items.append(new)

result = 1
print("[509, 487, 25, 511]")
print([v.inspected for v in monkeys])
for x in sorted([v.inspected for v in monkeys])[-2:]:
    # print(x)
    result *= x

print(result)





