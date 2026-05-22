class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        profit = 0
        for i in range(1, len(prices)):
            # potential candidate for new min_price
            if prices[i] > prices[i - 1]:
                min_price = min(prices[i - 1], min_price)
            profit = max(profit, prices[i] - min_price)
            print(profit, min_price, prices[i])

        return profit