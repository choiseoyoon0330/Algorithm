from collections import deque

n, k = map(int, input().split())
graph = []
data = []

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            data.append((graph[i][j], 0, i, j))

data.sort()
queue = deque(data)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

s, x, y = map(int, input().split())

while queue:
    a, b, c, d = queue.popleft()
    if b == s:
        break
    for i in range(4):
        nx = c + dx[i]
        ny = d + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = a
                queue.append((graph[nx][ny], b + 1, nx, ny))


print(graph[x - 1][y - 1])