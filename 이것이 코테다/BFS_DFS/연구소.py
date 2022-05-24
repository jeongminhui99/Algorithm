# https://www.acmicpc.net/problem/14502

n, m = map(int, input().split())
data = []
tmp = [[0] * m for _ in range(n)]

for _ in range(n):
    data.append(list(map(int, input().split())))

#4가지 이동 방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

def get_safe():
    score = 0
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 0:
                score += 1

    return score

#깊이 우선 탐색으로 이용해 바이러스 퍼뜨리기
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 상, 하, 좌, 우 가능한지 확인
        if nx >= 0 and nx < n and ny >= 0 and ny < m :
            if tmp[nx][ny] == 0:
                tmp[nx][ny] = 2
                virus(nx, ny)

#DFS를 이용해 울타리 설치면서 안전 구역 영역 계산
def dfs(count):
    global result
    if count == 3:
        for i in range(n):
            for j in range(m):
                tmp[i][j] = data[i][j]
        for i in range(n):
            for j in range(m):
                if tmp[i][j] == 2:
                    virus(i,j)
        result = max(result, get_safe())
        return 
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1
dfs(0)
print(result)