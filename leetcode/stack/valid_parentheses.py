class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {
            ")":"(",
            "]":"[",
            "}":"{"
        }
        
        # 스택 이용 예외 처리 및 일치 여부 판별
        for i in s:
            if i not in table:
                stack.append(i)
            elif not stack or stack.pop() != table[i]:
                return False
            
        return len(stack) == 0