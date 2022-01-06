## 풀이1) 리스트로 변환
import collections
from typing import Collection, Deque


def isPalidrome(self, s:str) -> bool :
    strs = []
    for char in s :
        if char.isalnum():
            strs.append(char.lower())
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False
    return True

## 풀이2) deque
from collections import deque

def isPalidrome(self, s:str) -> bool :
    strs: Deque = collections.deque()
    for char in s :
        if char.isalnum():
            strs.append(char.lower())
    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False
    return True

## 풀이3) 슬라이싱
import re
def isPalidrome(self, s:str) -> bool :
    s = s.lower()
    s = re.sub('[^a-z0-9]', '', s)

    return s == s[::-1]
