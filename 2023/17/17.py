#!/opt/homebrew/bin/python3
import heapq

f = open('17.txt', 'r')
lines = f.read().splitlines()

def solve(board, start, end, least, most):
    xs, ys = len(board), len(board[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] 

    pq = [(0, start[0], start[1], -1, 0, None)]
    visited = set()

    while pq:
        heat, x, y, prev_dir, moves, parent = heapq.heappop(pq)

        if (x, y) == end:
            return heat

        if (x, y, prev_dir, moves) in visited:
            continue
        visited.add((x, y, prev_dir, moves))

        for i, (dr, dc) in enumerate(directions):
            nx, ny = x + dr, y + dc
            if 0 <= nx < xs and 0 <= ny < ys:
                nh = heat + board[nx][ny]
                new_parent = (x, y, prev_dir, moves, parent)

                if prev_dir == i and moves < most:
                    heapq.heappush(pq, (nh, nx, ny, i, moves + 1, new_parent))
                elif (prev_dir + i) % 2 == 1 and (moves > least or prev_dir == -1):
                    heapq.heappush(pq, (nh, nx, ny, i, 1, new_parent))
    return 0

board = []
for l in lines:
    board.append([int(x) for x in l])


print(solve(board, (0, 0), (len(board) - 1, len(board[0]) - 1), 0, 3)) # part 1
print(solve(board, (0, 0), (len(board) - 1, len(board[0]) - 1), 3, 10)) # part 2