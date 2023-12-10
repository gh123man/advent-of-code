#!/opt/homebrew/bin/python3

f = open('5.txt', 'r')
lines = f.read().splitlines()
lines.append("")

seeds = []
ranges = []
inputRanges = []
outputRanges = []

def processSeed(seed):
    for inptIdex, r in enumerate(inputRanges):
        if seed in r:
            offset = r.index(seed)
            outputRange = outputRanges[inptIdex]

            if offset + outputRange.start in outputRange:
                return outputRange[offset]
    return seed

def makeOverlaps(input, output, mapRange):
    out = []
    diff = output.start - mapRange.start
    # no overlap left - no transform or overlap
    # |-----|
    #          |----|

    if input.start < output.start and input.stop < output.start:
        return [input], []

    # no overlap right - no transform or overlap
    #         |-----|
    # |----|
    if input.start > output.stop and input.stop > output.stop:
        return [input], []

    # contained within (or equal) - 1 range needs transform
    #    |---|
    #  |-------|
    if input.start >= output.start and input.stop <= output.stop:
        return [], [range(input.start - diff, input.stop - diff)]

    # input contains output - 3 ranges
    #  |-------|
    #    |---|
    if input.start < output.start and input.stop > output.stop:
        return [range(input.start, output.start), range(output.stop, input.stop)], [range(output.start - diff, output.stop - diff)]

    # end is contained - 2 ranges
    # |-----|
    #    |-----|
    if input.start < output.start and input.stop <= output.stop:
        return [range(input.start, output.start)], [range(output.start - diff, input.stop - diff)]

    # start is contained - 2 ranges
    #    |-----|
    # |-----|
    if input.start <= output.stop and input.stop > output.stop:
        return [range(output.stop, input.stop)], [range(input.start - diff, output.stop - diff)]

    return out


def processRanges(ranges):
    out = []
    for inptIdx, inptRange in enumerate(inputRanges):
        unmapped = []
        for r in ranges:
            # Process each range, returning unmapped and mapped ranges
            umapped, mapped = makeOverlaps(r, inptRange, outputRanges[inptIdx])
            out += mapped # we are done with the mapped ranges. 
            unmapped += umapped # re-process the unmapped ranges in the next step to see if they get mapped. 
        ranges = unmapped
    return out + ranges

for line in lines:
    if "seeds" in line:
        seeds = [int(x) for x in line.split(": ")[1].split()]

        for i in range(0, len(seeds), 2):
            ranges.append(range(seeds[i], seeds[i] + seeds[i + 1]))
    
    if len(line) > 0 and line[0].isdigit():
        dest, source, length = (int(x) for x in line.split())
        inputRanges.append(range(source, source + length))
        outputRanges.append(range(dest, dest + length))
        
    elif len(inputRanges) > 0:
        # Part 1
        seeds = [processSeed(seed) for seed in seeds]

        # Part 2
        ranges = processRanges(ranges)

        inputRanges = []
        outputRanges = [] 
# Part 1
print(min(seeds))
assert 510109797 == min(seeds)


# Part 2
print(min([x.start for x in ranges]))
assert 9622622 == min([x.start for x in ranges])