# <그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다.
# 철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다.
# 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다.
# <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 지도를 입력하여 단지수를 출력하고,
# 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오

# 첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.
# 시간 : 68ms

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]

# 인접한 곳에 집이 있는지 확인해 단지 형성 알아보기 위함
dx = [0,0,-1,1]
dy = [1,-1,0,0]


# dfs로 특정 노드 방문하고 연결된 모든 노드들을 방문
def dfs(x, y):
    global cnt
    # print(x, y, cnt)
    # 방문 처리
    visited[x][y] = True

    # 상하좌우 살펴보기
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        # 주어진 범위를 벗어나는 경우
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue

        # 인접 노드를 방문하지 않았고, 1이라면
        if not visited[nx][ny] and graph[nx][ny] == 1:
            # 재귀적으로 호출하면서 아파트 수 + 1
            cnt += 1
            dfs(nx, ny)


result = []
total = 0
for i in range(n):
    for j in range(n):
        cnt = 1
        # 방문하지 않고, 집이라면
        if not visited[i][j] and graph[i][j] == 1:
            total += 1
            dfs(i, j)
            result.append(cnt)

print(total)
result = sorted(result)
for i in result:
    print(i)