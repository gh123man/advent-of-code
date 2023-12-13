#!/opt/homebrew/bin/python3

f = open('13.txt', 'r')
lines = f.read().splitlines()
lines.append("")

def transpose(lines):
    transposed = []
    for y in range(len(lines[0])):
        row = []
        for x in range(len(lines)):
            row.append(lines[x][y])
        transposed.append("".join(row))
    return transposed

def diff(a, b):
    diff = 0
    for x, y in zip(a, b):
        if x != y:
            diff += 1
    return diff


def solve(nums, part2):
    for i in range(len(nums) - 1):
        maxDiff = 1 if part2 else 0
        if diff(nums[i], nums[i + 1]) <= maxDiff:
            a = nums[:i + 1][::-1]
            b = nums[i + 1:]
            maxDiff = 1 if part2 else 0

            while a and b:
                if diff(a[0], b[0]) <= maxDiff:
                    if part2 and diff(a[0], b[0]) == maxDiff:
                        maxDiff = 0
                    a.pop(0)
                    b.pop(0)
                else:
                    break
            if part2 and maxDiff == 0 and (not a or not b):
                return len(nums[:i + 1])
            elif not part2 and (not a or not b):
                return len(nums[:i + 1])
    return 0

def run(part2):
    buf = []
    ans = 0
    for line in lines:
        if line == "":
            a = solve(buf, part2)
            b = solve(transpose(buf), part2)
            if a > 0:
                ans += a * 100
            elif b > 0:
                ans += b

            buf = []
        else:
            buf.append(line)
    return ans

print(run(False))
print(run(True))
