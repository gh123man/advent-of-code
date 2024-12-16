from lib import *
import heapq

lines = lines("input.txt")

grid = Grid(lines)

def count_turns(d1, d2):
    index1 = cardinal_directions.index(d1)
    index2 = cardinal_directions.index(d2)
    return min((index2 - index1) % 4, (index1 - index2) % 4)


def score(steps, turns):
    return steps + (turns * 1000)

startDirection = cardinal_directions_map["E"]
start = grid.find("S")
end = grid.find("E")

def bfs(grid, start, end, startDirection):
    queue = [(score(0, 0), start, startDirection, 0, 0)]  
    bestScore = None
    visited = set()
    
    while queue:
        currentScore, pos, direction, steps, turns = heapq.heappop(queue)
        
        if pos == end:
            if bestScore is None or currentScore < bestScore:
                bestScore = currentScore
            continue
        
        if (pos, direction) in visited:
            continue
        visited.add((pos, direction))
        
        for nextPos, val, d in grid.neighbors(pos, cardinal_directions):
            if val is None or val == "#":
                continue
            newTurns = turns + count_turns(direction, d)
            newSteps = steps + 1
            newScore = score(newSteps, newTurns)
            
            if bestScore is not None and newScore >= bestScore:
                continue
            
            heapq.heappush(queue, (newScore, nextPos, d, newSteps, newTurns))
    
    return bestScore


def bfs2(grid, start, end, startDirection):
    queue = [(score(0, 0), start, startDirection, 0, 0, set())]  
    bestPaths = []
    bestScore = None
    visited = set()
    
    while queue:
        currentScore, pos, direction, steps, turns, posSet = heapq.heappop(queue)
        
        if pos == end:
            if bestScore is None or steps < bestScore:
                bestScore = steps
                bestPaths = [posSet]
            elif steps == bestScore:
                bestPaths.append(posSet)
            continue
        
        if (pos, direction) in visited:
            continue
        visited.add((pos, direction))
        
        for nextPos, val, d in grid.neighbors(pos, cardinal_directions):
            if val is None or val == "#":
                continue
            newTurns = turns + count_turns(direction, d)
            newSteps = steps + 1
            newScore = score(newSteps, newTurns)
            posSet.add(nextPos)
            
            if bestScore is not None and newScore >= bestScore:
                continue
            
            heapq.heappush(queue, (newScore, nextPos, d, newSteps, newTurns, posSet))
    
    print(len(bestPaths))
    return bestScore

# print(bfs(grid, start, end, startDirection))
print(bfs2(grid, start, end, startDirection))


