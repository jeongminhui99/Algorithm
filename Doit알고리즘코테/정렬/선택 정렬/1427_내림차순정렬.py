#https://www.acmicpc.net/problem/1427

import sys
print = sys.stdout.write
A = list(input())

for i in range(len(A)):
    m = i
    for j in range(i+1, len(A)):
        if A[j] > A[m]:
            m = j
    if A[i] < A[m]:
        tmp = A[i]
        A[i] = A[m]
        A[m] = tmp


for i in range(len(A)):
    print(A[i])