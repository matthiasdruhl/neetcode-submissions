class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l = 0
        for i in range(len(prices)):
            if prices[l] > prices[i]:
                l = i
            profit = max(prices[i] - prices[l], profit)

        return profit
