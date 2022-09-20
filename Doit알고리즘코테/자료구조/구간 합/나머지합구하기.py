#https://www.acmicpc.net/problem/10986

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
A = list(map(int, input().split()))
S = [0]*n #합 배열
C = [0]*m #같은 나머지의 인덱스 카운트
S[0] = A[0]
answer = 0
for i in range(1, n):
    S[i] = S[i-1] + A[i]

for i in range(n):
    remainder = S[i] % m
    if remainder == 0: 
        answer += 1
    C[remainder] += 1 # 나머지가 같은 인덱스의 개수 값 증가

for i in range(m):
    if C[i] > 1:
        answer += (C[i] * (C[i]-1) // 2)

print(answer)
