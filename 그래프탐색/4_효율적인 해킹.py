# 해커 김지민은 잘 알려진 어느 회사를 해킹하려고 한다. 이 회사는 N개의 컴퓨터로 이루어져 있다. 김지민은 귀찮기 때문에,
# 한 번의 해킹으로 여러 개의 컴퓨터를 해킹 할 수 있는 컴퓨터를 해킹하려고 한다.
# 이 회사의 컴퓨터는 신뢰하는 관계와, 신뢰하지 않는 관계로 이루어져 있는데,
# A가 B를 신뢰하는 경우에는 B를 해킹하면, A도 해킹할 수 있다는 소리다.
# 이 회사의 컴퓨터의 신뢰하는 관계가 주어졌을 때,
# 한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 출력하는 프로그램을 작성하시오.

# 시간 : 11188ms

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())    # 노드 개수, 간선 개수
# 양방향 그래프 X 일방향 그래프 O

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    # A가 B를 신뢰한다.
    graph[b].append(a)

# bfs 사용
def bfs(v):
    cnt = 1                    # 감염된 컴퓨터 수 (나 자신 포함)
    q = deque([v])             # q에 시작 노드를 넣어준다.
    # 모든 컴퓨터의 경우의 수 살펴 보아야 하기 때문에 방문처리를 함수 안으로 넣어 줌
    visited = [False] * (n + 1)
    visited[v] = 1             # 방문처리

    while q:
        node = q.popleft()     # 현재 살펴볼 노드
        for next_node in graph[node]:        # 현재 노드와 이어져 있는 모든 노드들 살피기
            if not visited[next_node]:       # 방문하지 않은 노드의 경우
                visited[next_node] = 1       # 방문처리
                cnt += 1                     # 감염된 컴퓨터 + 1
                q.append(next_node)          # 다음 노드로 이동하기 위해서 q에 담아주기

    return cnt

max_cnt = 0
result = []

# 모든 컴퓨터 경우의 수 살펴보기
for i in range(1, n+1):
    tmp = bfs(i)
    # 현재까지 최대 해킹 할 수 있는 컴퓨터보다 더 많은 경우,
    if tmp > max_cnt:
        max_cnt = tmp
        # 최대값으로 바꿔줘야하기 때문에 clear 해서 결과 값 넣었던 list 초기화 해준다
        result.clear()
        result.append(i)
    # 현재까지 최대 해킹 할 수 있는 컴퓨터와 같은 경우,
    elif tmp == max_cnt:
        # 결과값에 더해준다.
        result.append(i)
print(*result)