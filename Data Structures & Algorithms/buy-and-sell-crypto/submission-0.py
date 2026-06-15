class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        L = 0

        for R in range(len(prices)):
            profit = prices[R] - prices[L]
            if profit <= 0:
                L = R
            
            max_profit = max(max_profit, profit)
        return max_profit

        