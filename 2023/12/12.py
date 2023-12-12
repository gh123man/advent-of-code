#!/opt/homebrew/bin/python3

f = open('12.txt', 'r')
lines = f.read().splitlines()

memo = {}

# def getOptions(problem, c):
#     options = [] 
#     for p in range(len(problem) - c + 1):
#         cpy = list(problem)
#         for i in range(p):
#             cpy[i] = "."
#         for j in range(c):
#             cpy[p + j] = "#"
#         # print("".join(cpy))
#         options.append(("".join(cpy[:p + c]), "".join(cpy[p + c:])))
#         # print(problem, options)
#     return options

def isValidFwd(problem, size):
    l = 0
    i = 0
    for c in problem:
        if c == "#":
            l += 1
        elif l > 0:
            break
        i+= 1
    return l == size and not isValidFwd(problem[i:], size)


def getOptions(problem, c):
    options = [] 
    seen = set()
    for p in range(len(problem) - c + 1):
        cpy = list(problem)
        for i in range(p):
            if cpy[i] == "?":
                cpy[i] = "."
        for j in range(c):
            if cpy[p + j] != ".":
                cpy[p + j] = "#"
        cpy = "".join(cpy)
        if isValidFwd(cpy[:p + c], c) and cpy not in seen:
            options.append((cpy[:p + c], cpy[p + c:]))
            seen.add(cpy[:p + c])
        # print(problem, options)
    return options

def po(o):
    for a in o:
        # print("".join(a))
        print(a)
    
# po(getOptions("???.###", 1))
# po(getOptions("???.?.?#?", 2))
# po(getOptions("??#", 1))
# exit(0)


def isValidNext(problem, size):
    found = False
    i = 0
    for c in problem:
        if c == "#":
            found = True
        elif found:
            break
        i += 1

    l = 0
    for c in problem[i:]:
        if c == "#":
            l += 1
        elif l > 0:
            break
    return l == size

def isValidBkw(problem, size):
    l = 0
    for c in problem[::-1]:
        if c == "#":
            l += 1
        elif l > 0:
            break
    return l == size

def permute(parentProblem, problem, constraints):
    if len(constraints) == 0:
        if problem == "" or "#" not in problem:
            return 1, [problem]
        else:
            return 0, []

    dbg = []
    c = constraints.pop(0)
    opts = getOptions(problem, c) 

    if len(opts) == 0:
        return 0, []
    print(c, opts)

    sum = 0
    dbg = []
    for (lhs, subProblem) in opts:
        # print("validate", c, parentProblem , lhs)
        # if isValidNext(parentProblem + lhs, c):
        if len(parentProblem) == 0 or (len(parentProblem) > 0 and (parentProblem[-1] != "#" or lhs[0] != "#")):
            # print("validate YES", c, parentProblem , lhs)
            # print("YES", c, parentProblem + lhs)
            s, d = permute(lhs, subProblem, constraints.copy())
            sum += s
            for a in d:
                dbg.append(lhs + str(a))


    # print(sum, dbg)
    return sum, dbg


    
# print(isValid(".##", 1))
# print(isValid("###.", 2))
# print(isValid("#...", 2))
# print(getOptions("???", 2))
# print(getOptions("????#?#?..?#?", 4))
# exit()

# print(isValidFwd(".###", 3))



# po(getOptions("?###", 3))
# po(getOptions("?#??#", 2))
# po(getOptions(".#???#", 3))
# po(getOptions("?###????????", 3))
# po(getOptions(".#???#", 3))
# assert 1 == len(getOptions(".#???#", 3))
# assert 0 == len(getOptions(".#??#", 3))
# assert 1 == len(getOptions(".#?#", 3))
# print(getOptions("???????", 2))
# print(permute("???????", [2, 1]))
# print(permute("???", [1]))
# assert 3 == permute("???", [1])
# print(permute("????", [2]))
# assert 3 == permute("????", [2])

# v, dbg = permute("", "##????", [2, 1])
# print(v)
# for d in dbg:
#     print(d)
# assert 1 == permute("????", [2, 1])
# v, dbg = permute("", "?###????????", [3, 2, 1])
# v, dbg = permute("", "???.###", [1, 1, 3])
# v, dbg = permute("", ".??..??...?##.", [1, 1, 3])
# print(v)

v, dbg = permute("", "????#?#?..?#?", [4, 1])
# v, dbg = permute("", "??#", [1, 1])

print(v)
for d in dbg:
    print(d)



# """

# sum = 0
# for line in lines:
#     problem, constraint = line.split()
#     constraint = [int(x) for x in constraint.split(",")]
#     p, d = permute("", problem, constraint)
#     for x in d:
#         print(x)
#     sum  += p
#     print(p)

# print(sum)



# too high
# 8902