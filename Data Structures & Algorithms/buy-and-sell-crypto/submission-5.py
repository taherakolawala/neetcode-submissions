class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ptr1, ptr2 = 0, 1
        ret = 0
        while ptr2 < len(prices):
            if prices[ptr2] < prices[ptr1]:
                ptr1 = ptr2
                ptr2 += 1
                continue
            ret = max(ret, prices[ptr2] - prices[ptr1])
            ptr2 += 1
        return ret