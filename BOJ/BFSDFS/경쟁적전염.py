from collections import deque

n, k = map(int, input().split())

graph = []
data = [] #바이러스에 대한 정보를 담는 리스트

dx = [-1, 0, 1, 0]
dy = [0, 1, 0 -1]

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0 : #바이러스가 있을 때
            data.append(graph[i][j], 0, i, j) # (바이러스 종류, 시간, 위치 X, 위치 Y) 삽입
            
data.sort()
q = deque(data)

target_s, target_x, target_y = map(int, input().split())

while q:
    virus, s, x, y = q.popleft()
    if s == target_s:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx and nx < n and 0 <= ny and ny < n :
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, ))














