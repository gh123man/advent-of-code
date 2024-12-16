from copy import copy, deepcopy

# up, right, down, left
cardinal_directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
cardinal_directions_map = {"N": (-1, 0), "E": (0, 1), "S": (1, 0), "W": (0, -1)}

def lines(file):
    f = open(file, 'r')
    return f.read().splitlines()

class Grid:
    def __init__(self, lines=None):
        self.board = []
        if lines:
            self.parse(lines)

    def parse(self, lines):
        for line in lines:
            self.board.append(list(line))
        return self

    def copy(self):
        return deepcopy(self)
    
    def set(self, position, value):
        y, x = position
        self.board[y][x] = value
        return self
    
    def get(self, position):
        y, x = position
        if x < 0 or y < 0 or x >= len(self.board) or y >= len(self.board[x]):
            return None
        return self.board[y][x]
    
    def neighbors(self, pos, directions):
        for d in directions:
            next = (pos[0] + d[0], pos[1] + d[1])
            yield (next, self.get(next), d)

    def find(self, v):
        for y, row in enumerate(self.board):
            for x, cell in enumerate(row):
                if cell == v:
                    return (y, x)
        return None

    def __str__(self):
        return '\n'.join([''.join(row) for row in self.board])