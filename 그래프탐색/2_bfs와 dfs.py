# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
# 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.
# 시간 : 696ms


n, m, v = map(int, input().split())  #정점 개수, 간선 개수, 탐색 시작 번호
graph = [[False] * (n+1) for _ in range(n+1)]
# 양방향 그래프
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = True

# bfs 수행
from collections import deque

def bfs(v):
    global bfs_visited, graph
    q = deque([v])             # 시작 노드를 deque에 삽입
    bfs_visited[v] = True      # 방문처리

    while q:                   # q가 모두 없어질 때까지,
        node = q.popleft()     # 현재 탐색할 node
        bfs_result.append(node)

        for i in range(1, n+1):
            # node와 연결되어 있고, 아직 방문하지 않은 노드인 경우
            if not bfs_visited[i] and graph[node][i]:
                q.append(i)                # 연결된 노드 q에 넣기
                bfs_visited[i] = True      # 방문처리


# dfs 수행
def dfs(v):
    # 현재 노드 방문처리
    dfs_visited[v] = True
    dfs_result.append(v)

    # 현재 노드와 연결된 노드 중 방문 안한 가장 작은 수의 노드 재귀 함수로 찾기
    for i in range(1, n+1):
        if not dfs_visited[i] and graph[v][i]:
            dfs(i)

bfs_visited = [False] * (n+1)
dfs_visited = [False] * (n+1)

bfs_result = []
dfs_result = []
bfs(v)
dfs(v)

print(*dfs_result)
print(*bfs_result)

