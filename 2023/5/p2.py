#!/opt/homebrew/bin/python3

f = open('5.txt', 'r')
lines = f.read().splitlines()
lines.append("")

inputRanges = []
outputRanges = []
ranges = []

def mapRange(source, dest, transform):
    ranges = []
    if source[0] <= dest[0]:
        ranges.append(source[0])

    if source[1] <= dest[0]:
        ranges.append(source[1])

    if source[0] >= dest[0] and source[0] <= dest[1]:
        ranges.append(source[0])
    
    if source[0] >= dest[0] and source[0] <= dest[1]:
        ranges.append(source[0])



    




for line in lines:
    if "seeds" in line:
        seeds = [int(x) for x in line.split(": ")[1].split()]

        for i in range(0, len(seeds), 2):
            ranges.append((seeds[i], seeds[i] + seeds[i + 1]))
    
    if len(line) > 0 and line[0].isdigit():
        dest, source, length = (int(x) for x in line.split())
        inputRanges.append((source, source + length))
        outputRanges.append((dest, dest + length))
    elif len(inputRanges) > 0:
        newRanges = []

        print(ranges)
        print(inputRanges)
        print(outputRanges)


        inputRanges = []
        outputRanges = [] 
        exit(0)

