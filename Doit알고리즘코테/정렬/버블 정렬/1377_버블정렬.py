#https://www.acmicpc.net/problem/1377
import sys
input = sys.stdin.readline
n = int(input())
A = []

for i in range(n):
    A.append((int(input()), i))

sorted_A = sorted(A)
m = 0

#정렬 전 index - 정렬 후 index 계산의 최댓값 저장
for i in range(n):
    if m < sorted_A[i][1] - i:
        m = sorted_A[i][1] - i

print(m+1)