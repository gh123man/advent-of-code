#!/opt/homebrew/bin/python3

f = open('15.txt', 'r')
line = f.read().splitlines()[0]

def hash(code):
    hash = 0
    for c in code:
        hash = ((hash + ord(c)) * 17) % 256
    return hash

# Part 1
print(sum([hash(code) for code in line.split(",")]))

boxes = {}
for code in line.split(","):
    if code[-1] == "-":
        label = code[:-1]
        box = hash(label)

        if box in boxes:
            for i, l in enumerate(boxes[box]):
                if l[0] == label:
                    boxes[box].pop(i)
                    break

    else:
        label = code[:-2]
        val = code[-1]
        box = hash(label)

        if box not in boxes:
            boxes[box] = [(label, val)]
        else:
            isSet = False
            for i, l in enumerate(boxes[box]):
                if l[0] == label:
                    boxes[box][i] = (label, val)
                    isSet = True
            if not isSet:
                boxes[box].append((label, val))

keys = sorted(boxes.keys())
sum = 0
for key in keys:
    for i, box in enumerate(boxes[key]):
        sum +=  (int(key) + 1) * (i + 1) * int(box[1])

print(sum) # Part 2