class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        i = prices[0]

        for p in prices:
            if p < i:
                i = p
            profit = max(p - i, profit)
        return profit 