## 풀이1) 리스트로 변환
def isPalidrome(self, s:str) -> bool :
    strs = []
    for char in s :
        if char.isalnum():
            strs.append(char)
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False
    return True

## 풀이2) deque
## 풀이3) 슬라이싱
