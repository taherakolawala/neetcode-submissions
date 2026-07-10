class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        left = 0
        minPrice = float('inf')
        for right in range(len(prices)):
            best = max(best, prices[right] - prices[left])
            if prices[right] < minPrice:
                minPrice = prices[right]
                left = right
        return best
