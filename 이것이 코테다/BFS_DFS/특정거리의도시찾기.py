# https://www.acmicpc.net/problem/18352

# BFS 활용
# 최단 거리 저장

from collections import deque
import sys

def bfs(graph, start, distance):
    queue = deque([start])
    visited[start] = True
    while queue:
        now = queue.popleft()
        for i in graph[now]:
            if not visited[i]:
                distance[i] = distance[now] + 1
                queue.append(i)
                visited[i] = True


input = sys.stdin.readline
# N 도시 수, M 도로 수, K 거리 정보 X 출발 도시
n, m, k, x = map(int, input().split(' '))
graph = [[] for _ in range(n+1)] 

for _ in range(m):
    a, b =  map(int, input().split(' ')) 
    graph[a].append(b)

visited = [False] * (n+1)
distance = [0] * (n+1)

bfs(graph, x, distance)

check = False
for i in range(len(distance)):
    if distance[i] == k:
        print(i)
        check = True
if check == False:
    print(-1)