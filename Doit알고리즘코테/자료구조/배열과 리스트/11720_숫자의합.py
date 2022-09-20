#백준 11720번
#https://www.acmicpc.net/problem/11720

n = input()
numbers = list(input())
sum = 0

for i in numbers:
    sum += int(i)

print(sum)