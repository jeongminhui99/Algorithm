class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_price = 0 # 어차피 최댓값은 0보다 커야하기 때문에
        min_price = sys.maxsize
        
        #최댓값과 최댓값을 계속 갱신
        for price in prices:
            min_price = min(min_price, price)
            max_price = max(max_price, price - min_price)
        
        return max_price