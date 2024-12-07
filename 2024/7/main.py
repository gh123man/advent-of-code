#!/opt/homebrew/bin/python3 

f = open('input.txt', 'r')
lines = f.read().splitlines()

def solve(target, current, remaining, part2):
    if current > target:
        return False
    if remaining == []:
        if target == current:
            return True
        return False
    
    copy = remaining.copy()
    next = copy.pop(0)
    if part2:
        return solve(target, current * next, copy, part2) or solve(target, int(str(current) + str(next)), copy, part2) or solve(target, current + next, copy, part2) 
    else:
        return solve(target, current * next, copy, part2) or solve(target, current + next, copy, part2) 

sum = 0
sum2 = 0
for line in lines:
    answer, nums = line.split(":")
    nums = [int(x) for x in nums.split()]
    if solve(int(answer), nums[0], nums[1:], False):
        sum += int(answer)
    if solve(int(answer), nums[0], nums[1:], True):
        sum2 += int(answer)
    
# Part 1
print(sum)
# Part 2
print(sum2)



