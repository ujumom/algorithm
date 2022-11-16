# 루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.
# 트리 상에서 연결된 두 정점이 주어진다.

# 제한이 없는 경우 시간 초과 걸린다
# 시간 : 408ms
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

n = int(input())
tree = [[] * (n+1) for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
    # [[], [6, 4], [4], [6, 5], [1, 2, 7], [3], [1, 3], [4]]


def dfs(v, parent):
    # 현재 노드의 부모 노드 기록
    result[v] = parent
    visited[v] = True           # 현재 노드 방문 처리

    # 더 이상 연결된 노드가 없는 경우 return
    if not tree[v]:
        return

    # 현재 노드와 연결된 노드로 이동
    for node in tree[v]:
        # 방문하지 않고, 부모 노드가 아닌 노드로 이동
        if not visited[node] and node != parent:
            dfs(node, v)

result = [0] * (n+1)
visited = [False] * (n+1)

dfs(1, 0)
for i in range(2, n+1):
    print(result[i])


from collections import deque
def bfs():
    q = deque([1])

    while q:
        node = q.popleft()
        # 현재 노드와 연결된 노드들에서
        for i in tree[node]:
            # 아직 부모가 기록되지 않은 노드는, 부모 기록 해주기
            if result[i] == 0:
                result[i] = node
                q.append(i)

bfs()