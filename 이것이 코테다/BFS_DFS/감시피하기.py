from itertools import combinations

n = int(input())
board = [] #복도 정보
teachers = [] # 모든 선생님의 위치 정보
spaces = [] # 모든 빈 공간 위치 정보

for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        if board[i][j] == 'T':
            teachers.append((i,j))
        if board[i][j] == 'X':
            spaces.append((i,j))

def watch(x, y, direction):
    #왼쪽
    if direction == 0:
        while y >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y -= 1
    if direction == 1: # 오른쪽
        while y < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y += 1
    if direction == 2: # 위
        while x >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x -= 1
    if direction == 3: # 아래
        while x < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x += 1
    return False

# 장애물 설치 이후에, 한명이라도 학생이 감지되는지 검사
def process():
    for x, y in teachers:
        for i in range(4): # 4가지 방향으로 감지
            if watch(x, y, i):
                return True
    return False #감지 못함


find = False

#빈 공간에서 3개를 뽑는 모든 조합을 확인
for data in combinations(spaces, 3):
    #장애물 설치
    for x, y in data:
        board[x][y] = 'O'
    # 학생이 한명도 발견되지 않는 경우
    if not process():
        find = True
        break
    for x, y in data:
        board[x][y] = 'X'

if find:
    print('YES')
else:
    print('No')
