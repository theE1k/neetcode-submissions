class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1: return 0
        buy = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            if buy > prices[i]:
                buy = prices[i]
            else:
                sell = prices[i]
                profit = max(sell-buy,profit)
        return profit
        