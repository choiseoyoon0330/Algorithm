import sys
input = sys.stdin.readline

n, m = map(int, input().split())
x, y, d = map(int, input().split())
visited = [[0] * m for _ in range(n)]
visited[x][y] = 1

maps = []
for i in range(n):
    maps.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 1
turn = 0

def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3

while True:
    turn_left()
    nx = x + dx[d]
    ny = y + dy[d]
    if visited[nx][ny] == 0 and maps[nx][ny] == 0:
        visited[nx][ny] = 1
        x = nx
        y = ny
        result += 1
        turn = 0
        continue
    else:
        turn += 1
    if turn == 4:
        nx = x - dx[d]
        ny = y - dy[d]
        if maps[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn = 0

print(result)