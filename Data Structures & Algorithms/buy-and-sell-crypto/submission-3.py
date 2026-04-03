class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        maxProfit = 0

        for right in range(len(prices)):
            if prices[left] > prices[right]:
                left = right
                continue

            maxProfit = max(maxProfit, prices[right] - prices[left])

        return maxProfit
            