

content = open('1.txt', 'r').read()
subs = [[int(n) for n in x.split("\n")] for x in content.split("\n\n")] 
sums = list(map(lambda x: sum(x), subs))
sums.sort()
print(sums[-1])
print(sum(sums[-3:]))