from lib import *
import heapq
from collections import deque
import sys

sys.setrecursionlimit(1500000) 

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

# Thanks chatGPT
def dijkstra(grid, start, end, startDirection):
    visited = set()
    dist = {}
    prev_states = {} 
    
    start_state = (start, startDirection)
    dist[start_state] = 0
    pq = [(0, start, startDirection, 0, 0)]

    while pq:
        currentScore, pos, direction, steps, turns = heapq.heappop(pq)
        state = (pos, direction)
        if state in visited:
            continue
        visited.add(state)
        
        if pos == end:
            continue

        for nextPos, val, d in grid.neighbors(pos, cardinal_directions):
            if val is None or val == "#":
                continue
            new_turns = turns + count_turns(direction, d)
            new_steps = steps + 1
            new_score = score(new_steps, new_turns)
            next_state = (nextPos, d)

            if next_state not in dist or new_score < dist[next_state]:
                dist[next_state] = new_score
                prev_states[next_state] = [state]
                heapq.heappush(pq, (new_score, nextPos, d, new_steps, new_turns))
            elif new_score == dist[next_state]:
                prev_states[next_state].append(state)

    end_states = [s for s in dist if s[0] == end]

    if not end_states:
        return set()

    min_end_cost = min(dist[s] for s in end_states)
    optimal_end_states = [s for s in end_states if dist[s] == min_end_cost]

    to_visit = optimal_end_states[:]
    all_optimal_positions = set(s[0] for s in to_visit)

    while to_visit:
        cur = to_visit.pop()
        if cur in prev_states:
            for p in prev_states[cur]:
                if p[0] not in all_optimal_positions:
                    all_optimal_positions.add(p[0])
                to_visit.append(p)

    return all_optimal_positions

print(bfs(grid, start, end, startDirection))
poss = dijkstra(grid, start, end, startDirection)
print(len(poss))

