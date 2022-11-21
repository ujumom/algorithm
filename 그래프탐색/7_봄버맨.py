import sys
from collections import deque

# 시뮬레이션은 차근차근 단계를 밟아가는 것이 중요하다.
# 핵심 1 ) 기존 폭탄의 위치를 기억 하기 위해 deque를 사용하면 된다.
# 핵심 2 ) while문은 조건문에 해당하더라도 while 끝까지 실행한다! 따라서 중간에 break로 빠져나올 필요가 있다.

r, c, n = map(int, sys.stdin.readline().split())
# 1단계: 가장 처음에 봄버맨은 일부 칸에 폭탄을 설치해 놓는다. 모든 폭탄이 설치된 시간은 같다.
graph = [list(map(str, sys.stdin.readline().strip())) for _ in range(r)]

cnt = 0
# 2단계: 다음 1초 동안 봄버맨은 아무것도 하지 않는다.
cnt += 1

# 3단계, 4단계 반복
while cnt < n:
    # 2.5단계 : 3단계 (모두 폭탄 설치) 를 대비해 폭탄의 위치를 저장 해야 한다.
    bomb = deque()

    for i in range(r):
        for j in range(c):
            if graph[i][j] == "O":
                bomb.append((i, j))

    # 3단계 : 다음 1초 동안 폭탄이 설치 되어 있지 않은 모든 칸에 폭탄을 설치한다.
    for i in range(r):
        for j in range(c):
            if graph[i][j] != "O":
                graph[i][j] = "O"

    cnt += 1      # 1
    # while 문은 끝까지 돌고 조건문에 걸리는 경우에 끝내 버리기 때문에
    # 중간에 break 꼭 넣어 줘야한다.
    if cnt == n:
        break

    # 4단계: 1초가 지난 후에 3초 전에 설치된 폭탄이 모두 폭발한다.
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while bomb:
        a, b = bomb.popleft()
        # 폭탄이 있던 자리를 파괴
        graph[a][b] = "."

        # 폭탄이 있던 자리의 상하좌우도 파괴
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]

            # 범위를 벗어나지 않는 경우
            if 0 <= x < r and 0 <= y < c:
                # 상하좌우에
                # 칸이 비어있으면 check 안해도 되기 때문에
                # 폭탄이 있는 경우만 빈칸으로 만들어준다.
                if graph[x][y] == "O":
                    graph[x][y] = "."
    # 1초 경과!
    cnt += 1

for i in graph:
    print("".join(i))