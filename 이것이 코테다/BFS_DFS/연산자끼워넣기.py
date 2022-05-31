# 중복 순열(product)
# from itertools import product

# n = 4
# print(list(product(['+', '-', '*', '/'], repeat=(n-1))))

n = int(input())
#연산을 수행하고하는 수 리스트
data = list(map(int, input().split()))
#연산자 개수, + - * /
add, sub, mul, div = map(int, input().split())

# 최솟값, 최댓값 초기화
min_value = 1e9
max_value = -1e9

# DFS
def dfs(i, now):
    global min_value, max_value, add, sub, mul, div
    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else:
        if add > 0:
            add -= 1
            dfs(i+1, now+data[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i+1, now-data[i])
        if mul > 0:
            mul -= 1    
            dfs(i+1, now*data[i])
        if div > 0:
            div -= 1
            dfs(i+1, int(now/data[i]))

dfs(1, data[0])
print(max_value)
print(min_value)

