class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ret = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                ret = max(ret, prices[j] - prices[i])
                print('i: ', prices[i], ' j: ', prices[j], ' i-j: ', prices[j] - prices[i], ' max: ' , ret)

        return ret