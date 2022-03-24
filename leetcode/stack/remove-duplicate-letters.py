import collections

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        #집합으로 정렬
        for char in sorted(set(s)):
            suffix = s[s.index(char):]
            if set(s) == set(suffix):
                return char + self.removeDuplicateLetters(suffix.replace(char, ''))
        return ''

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter, seen, stack = collections.Counter(s), set(), []
        
        for char in s:
            counter[char] -= 1
            if char in seen: # 이미 처리된 문자 여부를 확인하기 위해
                continue
            # 뒤에 붙일 문자가 있다면 스택에서 제거
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)
        return ''.join(stack)
        