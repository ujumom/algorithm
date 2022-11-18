r,c,n = map(int, input().split())
graph = [list(input()) for _ in range(r)]

# 총 R개의 줄에 N초가 지난 후의 격자판 상태를 출력한다.

# 폭탄이 있는 칸은 3초가 지난 후에 폭발하고, 폭탄이 폭발한 이후에는 폭탄이 있던 칸이 파괴되어 빈 칸이 되며,
# 인접한 네 칸도 함께 파괴된다. 즉, 폭탄이 있던 칸이 (i, j)인 경우에 (i+1, j), (i-1, j), (i, j+1), (i, j-1)도 함께 파괴된다.
# 만약, 폭탄이 폭발했을 때, 인접한 칸에 폭탄이 있는 경우에는 인접한 폭탄은 폭발 없이 파괴된다. 따라서, 연쇄 반응은 없다.

# 가장 처음에 봄버맨은 일부 칸에 폭탄을 설치해 놓는다. 모든 폭탄이 설치된 시간은 같다.
# 다음 1초 동안 봄버맨은 아무것도 하지 않는다.
# 다음 1초 동안 폭탄이 설치 되어 있지 않은 모든 칸에 폭탄을 설치한다. 즉, 모든 칸은 폭탄을 가지고 있게 된다. 폭탄은 모두 동시에 설치했다고 가정한다.
# 1초가 지난 후에 3초 전에 설치된 폭탄이 모두 폭발한다.
# 3과 4를 반복한다.

# n이 짝수면 전체가 다 '0'이고
# n이 홀수인 경우 일일히 2가지로 패턴이 나뉨

another_graph = [list('O'*c) for _ in range(r)]

# 두번째 패턴
dx = [0,0,-1,1]
dy = [1,-1,0,0]

cnt = 0

def dfs():
    pass

while True:
    # 시간 경과
    cnt += 1

    for i in range(r):
        for j in range(c):
            if graph[i][j] == 'O':
                # 자기자신 빈칸
                another_graph[i][j] = '.'
                # 상하좌우 모두 빈칸
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if nx < 0 or ny < 0 or nx >= r or ny >= c:
                        continue
                    another_graph[nx][ny] = '.'

    # 찾는 시간이 된 경우,
    if cnt == n:
        break


zero_graph = [list('O'*c) for _ in range(r)]
# 홀수인 경우
if n % 2:
    if n % 4 == 1:
        for i in graph:
            print("".join(i))
    elif n % 4 == 3:
        for i in another_graph:
            print("".join(i))
else:
    for i in zero_graph:
        print("".join(i))
