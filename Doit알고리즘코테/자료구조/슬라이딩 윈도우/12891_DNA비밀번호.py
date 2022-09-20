#https://www.acmicpc.net/problem/12891
checkList = [0] * 4
myList = [0] * 4
check = 0

def myadd(c):
    global checkList, myList, check
    if c == 'A':
        myList[0] += 1
        if myList[0] == checkList[0]:
            check += 1
    elif c =="C":
        myList[1] += 1
        if myList[1] == checkList[1]:
            check += 1
    elif c == "G":
        myList[2] += 1
        if myList[2] == checkList[2]:
            check += 1
    elif c == "T":
        myList[3] += 1
        if myList[3] == checkList[3]:
            check += 1

def myremove(c):
    global checkList, myList, check
    if c == 'A':
        if myList[0] == checkList[0]:
            check -= 1
        myList[0] -= 1
    elif c =="C":
        if myList[1] == checkList[1]:
            check -= 1
        myList[1] -= 1
    elif c == "G":
        if myList[2] == checkList[2]:
            check -= 1
        myList[2] -= 1
    elif c == "T":
        if myList[3] == checkList[3]:
            check -= 1
        myList[3] -= 1


S, P = map(int, input().split())
A = list(input())
checkList = list(map(int, input().split()))
result = 0


for i in range(4):
    if checkList[i] == 0:
        check += 1

for i in range(P):
    myadd(A[i])

if check == 4:
    result += 1

for i in range(P, S): # 2,3
    j = i - P #부분문자열의 길이 = p = i - j
    myadd(A[i])
    myremove(A[j])
    if check == 4:
        result += 1

print(result)