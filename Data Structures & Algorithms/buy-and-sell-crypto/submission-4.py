class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        low = prices[0]
        high = prices[0]
        for p in prices:
            if p < low:
                low = p
                high = p
            elif p > high:
                high = p
                profit = max(profit, high - low)
               
                
        return profit