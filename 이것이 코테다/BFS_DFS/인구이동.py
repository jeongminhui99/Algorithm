from collections import deque

n, l, r = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

result = 0

def bfs(x, y, index):
    united = [] #(x,y) 위치와 연결된 나라 (연합) 정보를 담는 리스트
    united.append((x,y))
    q = deque()
    q.append((x,y))
    union[x][y] = index # 현재 연합의 번호 할당
    summary = graph[x][y] # 현재 연합의 전체 인구 수 
    count = 1 # 현재 연합 국가의 수
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                if l <= abs(graph[nx][ny]-graph[x][y]) <= r:
                    q.append((nx, ny))
                    union[nx][ny] = index
                    summary += graph[nx][ny]
                    count += 1
                    united.append((nx, ny))
    #연합 국가끼리 인구를 분배
    for i, j in united:
        graph[i][j] = summary // count
    return count


total_count = 0

while True: # 더 이상 인구 이동을 할 수 없을 때까지 반복
    union = [[-1] * n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1: #해당 나라가 아직 처리되지 않았다면
                bfs(i, j, index)
                index += 1
    # 모든 인구 이동이 끝난 경우
    if index == n*n:
        break
    total_count += 1

print(total_count)
