#https://www.acmicpc.net/problem/1874

N = int(input())
A = [0]*N

for i in range(N):
    A[i] = int(input())

answer = []
stack = []
num = 1
result = True
for i in range(N):
    s = A[i]
    if s >= num:
        while s >= num:
            stack.append(num)
            num += 1
            answer.append("+")
        stack.pop()
        answer.append("-")
    else:
        if stack.pop() != s:
            print("NO")
            result = False
            break
        else:
            answer.append("-")

if result:
    for a in answer:
        print(a)
