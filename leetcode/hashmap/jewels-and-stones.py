import collections

# [ 풀이 1 ] 해시 테이블을 이용한 풀이
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs = {}
        count = 0
        
        # S의 빈도 수 계산
        for char in stones:
            if char not in freqs:
                freqs[char] = 1
            else:
                freqs[char] += 1
        
        # J의 빈도 수 합산
        for char in jewels:
            if char in freqs:
                count += freqs[char]
        return count

# [ 풀이 2 ] defulatdict를 이용한 비교 생략
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs = collections.defaultdict(int)
        count = 0
        
        # 비교 없이 돌의 빈도 수 계산
        for char in stones:
            freqs[char] += 1
        
        # 비교 없이 보석의 빈도 수 합산
        for char in jewels:
            count += freqs[char]
            
        return count

# [ 풀이 3 ] Counter로 계산 생략
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs = collections.Counter(stones) #돌의 빈도 수 계산
        count = 0
        
        # 비교 없이 보석의 빈도 수 합산
        for char in jewels:
            count += freqs[char]
            
        return count

# [ 풀이 4 ] 파이썬다운 방식
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # [s for s in stones] -> ['a', 'A', ....]
        # [s in jewels for s in stones] -> [True, True, ...]
        return sum(s in jewels for s in stones)