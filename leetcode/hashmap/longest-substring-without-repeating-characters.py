class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        max_length = start = 0
        # start, index 모두 왼쪽에서 시작하고 index는 다음과 같이 계속 오른쪽으로 확장한다.
        for index, char in enumerate(s):
            #이미 등장했던 문자이면 start 위치 갱신
						# 슬라이딩 윈도우 범위 안에 있는 문자가 아닌 경우는 무시
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:
                max_length = max(max_length, index - start + 1)
            
            # 현재 문자를 키로 하는 해시 테이블로 현재 위치를 값으로 삽입한다.
            used[char] = index
        
        return max_length