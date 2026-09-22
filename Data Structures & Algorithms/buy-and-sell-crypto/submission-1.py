class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float("inf")
        profit = 0
        for i in range(0, len(prices)):
            profit = max(profit, prices[i] - buy)
            buy = prices[i] if prices[i] < buy else buy
            

        return 0 if profit == 0 else profit


        
        
