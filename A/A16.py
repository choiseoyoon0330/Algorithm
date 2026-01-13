from collections import deque
from itertools import combinations

n, m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

space = []
virus = []

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            space.append((i, j))
        elif graph[i][j] == 2:
            virus.append((i, j))

def virus_spread(temp):
    queue = deque(virus)
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                temp[nx][ny] = 2
                queue.append((nx, ny))

def get_score(temp):
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

result = 0

for walls in combinations(space, 3):
    temp = [row[:] for row in graph]

    for x, y in walls:
        temp[x][y] = 1

    virus_spread(temp)
    result = max(result, get_score(temp))

print(result)