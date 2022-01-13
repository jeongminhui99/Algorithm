# 주어진 리스트를 1부터 n까지 만드는데 수정해야할 최소 횟수?

def solution_f(A):
    A.sort()
    result = 0
    idx = 1
    for v in A:
        diff = v - idx
        if diff < 0 :
            result -= diff
        elif diff > 0 :
            result += diff
        idx += 1
    return result
print(solution_f([6,2,3,5,6,3]))