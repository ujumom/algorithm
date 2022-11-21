from collections import deque

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
res = 0

q = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append([i, j])

# print(q) : deque([[0, 0], [3, 5]])

def bfs(graph):
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append([nx, ny])

bfs(graph)
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(-1)
            exit()
        res = max(res, graph[i][j])
print(res-1)