#https://www.acmicpc.net/problem/17298

n = int(input())
A = list(map(int, input().split()))
answer = [0] * n
stack = []

for i in range(n):
    while stack and A[stack[-1]] < A[i]:
        answer[stack.pop()] = A[i]
    stack.append(i)

while stack:
    answer[stack.pop()] = -1

result = ''
for i in range(n):
    result += str(answer[i])+" "
print(result)