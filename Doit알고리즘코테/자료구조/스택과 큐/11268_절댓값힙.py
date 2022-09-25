#https://www.acmicpc.net/problem/11286
import sys
from queue import PriorityQueue #우선순위 큐

print = sys.stdout.write
input = sys.stdin.readline

N = int(input())
myqueue = PriorityQueue()

for i in range(N):
    request = int(input())
    if request == 0:
        if myqueue.empty():
            print('0\n')
        else:
            tmp = myqueue.get()
            print(str(tmp[1]) + '\n')
    else:
        #절댓값 -> 음수 우선 정렬 (데이터의 순서가 정렬의 우선순위가 된다.)
        myqueue.put((abs(request), request))

# 우선순위 큐 정렬기준 변경 사용법
# que.put((3, 'Apple'))
# que.put((1, 'Banana'))
# que.put((2, 'Cherry'))

# print(que.get()[1])  # Banana
# print(que.get()[1])  # Cherry
# print(que.get()[1])  # Apple