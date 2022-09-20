#https://www.acmicpc.net/problem/11659

import sys

input = sys.stdin.readline
suNo, quizNo = map(int, input().split())
numbers = list(map(int, input().split()))
prefix_sum = [0] #합 배열 
temp = 0

for i in numbers:
    temp += i
    prefix_sum.append(temp)

for i in range(quizNo):
    s, e = map(int, input().split())
    print(prefix_sum[e] - prefix_sum[s-1])

