# Problem Link: https://www.hackerearth.com/practice/algorithms/graphs/breadth-first-search/practice-problems/algorithm/ujjwals-mine-9eacab11/
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs_util(grid, size, start):
    dist = [[0 for i in range(size)] for j in range(size)]
    Q = deque()
    visited = set()
    Q.append(start)
    visited.add(start)
    while len(Q) != 0:
        cell = Q.popleft()
        for i in range(4):
            x,y = cell[0]+dx[i], cell[1]+dy[i]
            if x<0 or y<0 or x>=size or y>=size or grid[x][y] == '#':
                continue
            if (x,y) not in visited:
                visited.add((x,y))
                dist[x][y] = dist[cell[0]][cell[1]] + 1
                Q.append((x,y))
    return dist

def solve(grid, size):
    mine1, mine2 = 0, 0
    player1, player2 = 0,0
    for i in range(size):
        for j in range(size):
            if grid[i][j] == '*':
                if mine1 == 0:
                    mine1 = (i, j)
                else:
                    mine2 = (i, j)
            if grid[i][j] == '^':
                if player1 == 0:
                    player1 = (i,j)
                else:
                    player2 = (i,j)

    dist1 = bfs_util(grid, size, player1)
    dist2 = bfs_util(grid, size, player2)

    player1_mine1 = dist1[mine1[0]][mine1[1]]
    player1_mine2 = dist1[mine2[0]][mine2[1]]

    player2_mine1 = dist2[mine1[0]][mine1[1]]
    player2_mine2 = dist2[mine2[0]][mine2[1]]

    min_time = min(max(player1_mine1, player2_mine2), max(player1_mine2, player2_mine1))

    return min_time

if __name__ == '__main__':
    testcases = int(input())
    for _ in range(testcases):
        size = int(input())
        grid = []
        for i in range(size):
            grid.append(input())
        min_time = solve(grid, size)
        if min_time == 0:
            print('No')
        else:
            print('Yes')
            print(min_time)
