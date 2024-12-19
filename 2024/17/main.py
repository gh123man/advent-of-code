from lib import *
from copy import copy

lines = lines("input.txt")

class Computer():

    def __init__(self, A, B, C, program):
        self.A = A
        self.B = B
        self.C = C
        self.ip = 0
        self.program = program
        self.result = []
        self.i = 0
    
    def eval(self):
        if self.ip >= len(self.program):
            return False
        op = self.program[self.ip]
        operand = self.program[self.ip + 1]

        if op == 0:
            self.A = self.A // (2 ** self.combo(operand))
        if op == 1:
            self.B = self.B ^ operand
        if op == 2:
            self.B = self.combo(operand) % 8 
        if op == 3 and self.A != 0:
            self.ip = operand
            return True
        if op == 4:
            self.B = self.B ^ self.C
        if op == 5:
            ans = self.combo(operand) % 8
            self.result.append(ans)
        if op == 6:
            self.B = self.A // (2 ** self.combo(operand))
        if op == 7:
            self.C = self.A // (2 ** self.combo(operand))

        self.ip += 2
        return True
                

    
    def reset(self):
        self.A = self.i
        self.B = 0
        self.C = 0
        self.ip = 0
        print(self)
        return True


    def combo(self, op):
        if op in range(0, 4):
            return op 
        if op == 4: return self.A
        if op == 5: return self.B
        if op == 6: return self.C
        return None
    
    def __str__(self):
        return f"A: {oct(self.A)},\n B: {oct(self.B)},\n C: {oct(self.C)},\n"
        pass

A = int(lines[0].split(":")[1])
B = int(lines[1].split(":")[1])
C = int(lines[2].split(":")[1])
nums = [int(x) for x in lines[4].split(": ")[1].split(",")]

print(A, B, C, nums)

# part 1
comp = Computer(A, B, C, nums)
while comp.eval():
    continue
print(comp.result)


i = 0
n = len(nums) - 1
while True:
    comp = Computer(i, 0, 0, nums)
    while comp.eval():
        continue

    if comp.result == nums[n:]:
        print(comp.result)
        if n == 0:
            print(i)
            exit(0)
        i *= 8
        n -= 1
        continue
    i += 1



