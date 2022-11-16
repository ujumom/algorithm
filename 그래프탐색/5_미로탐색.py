# 미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다.
# 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오.
# 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.
# 위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.
# 시간 : 116ms
from collections import deque

# 최소의 거리를 구하는 경우 bfs 사용해서 이동하면서 노드의 번호를 지나온 칸 수로 바꾸어 준다.
n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(x,y):
    q = deque()
    q.append((x,y))                 # 0,0에서 탐색 시작

    while q:
        x, y = q.popleft()          # 살펴볼 노드

        # 해당 노드와 인접한 노드중에서
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위를 벗어나지 않고,
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 이동 할 수 있는 노드
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                # 지금까지 왔던 거리 + 1
                graph[nx][ny] = graph[x][y] + 1

                # 인접한 모든 노드를 다 q에 넣는다.
                q.append((nx, ny))

    # 마지막까지 움직인 최소한의 칸의 수 출력
    return graph[n-1][m-1]

print(bfs(0,0))