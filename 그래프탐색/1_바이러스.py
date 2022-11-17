# 양방향 그래프
# 1번 노드에서 시작 해 연결 된 모든 노드의 갯수를 출력 하면 된다.
# 깊이우선탐색으로 풀어도 되고, 넓이우선탐색으로 풀어도 된다.

# 1. dfs 로 풀이 : 84ms
# 1) 탐색 시작 노드를 스택에 삽입하고 방문 처리
# 2) 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에서 꺼내고
# 방문처리 한다. 방문하지 않는 인접 노드가 없으면 스택에서 최상단 노드를 꺼냅니다.
# 3) 2번 과정 수행할 수 없을 때까지 반복

# n = int(input())
# m = int(input())
# # 각 노드가 연결된 정보를 2차원 리스트로 표현
# graph = [[False] * (n + 1) for _ in range(n+1)]
#
# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a][b] = True
#     graph[b][a] = True
#
#
# def dfs(start):
#     global cnt, visited
#     visited[start] = True
#     # 해당하는 노드에서 연결되어 있는 모든 노드들 살펴보기
#     for i in range(1, n+1):
#         # 현재 노드와 연결되어있는 노드이면서 방문하지 않은 노드라면
#         if graph[start][i] == True and not visited[i]:
#             cnt += 1                  # 감염된 노드 + 1
#             dfs(i)                    # 연결된 노드를 재귀적으로 방문
#
#
# # 1번 노드에서 시작
# cnt = 0
# visited = [False]*(n+1)
# dfs(1)
#
# print(cnt)

# 2. bfs로 풀이 : 시간 108ms

# 가까운 노드부터 우선적으로 탐색
# 1) 탐색 시작 노드를 큐에 삽입하고 방문처리
# 2) 큐에서 노드를 꺼낸 다음 해당 노드의 인접 노드 중 방문하지 않은 모든 노드 큐에 삽입하고 방문처리
# 3) 2번과정 계속 반복


from collections import deque
n = int(input())
m = int(input())
# 각 노드가 연결된 정보를 2차원 리스트로 표현
graph = [[False] * (n + 1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

q = deque()

def bfs(start):
    global cnt

    # 1) 탐색 시작 노드를 큐에 삽입하고 방문처리
    visited[start] = True
    q.append(start)

    # 2) 큐에서 노드를 꺼낸 다음 해당 노드의 인접 노드 중 방문하지 않은 모든 노드 큐에 삽입하고 방문처리
    while q:
        v = q.popleft()
        for i in range(1, n+1):
            if graph[v][i] == True and not visited[i]:
                q.append(i)
                cnt += 1
                visited[i] = True

cnt = 0
visited = [False] * (n + 1)
bfs(1)
print(cnt)