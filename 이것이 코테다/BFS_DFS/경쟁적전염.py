from collections import deque

n, k = map(int, input().split())

graph = [] #전체 보드 정보를 담는 리스트
data = [] #바이러스에 대한 정보를 담는 리스트

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0 : #바이러스가 존재한다면
            data.append((graph[i][j], 0, i, j)) # 바이러스 종류, 시간, 위치 X, 위치 Y

data.sort() # 같은 시간에서 시작 낮은 바이러스 부터
q = deque(data)

target_s, target_x, target_y = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


# BFS 탐색
while q:
    print(q)
    virus, s, x, y = q.popleft()
    if s == target_s:
        break
    #현재 노드에서 주변 4가지 위치를 각각 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        #해당 위치로 이동할 수 있는 경우
        if 0 <= nx and nx < n and 0 <= ny and ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s+1, nx, ny))

print(graph[target_x-1][target_y-1])





