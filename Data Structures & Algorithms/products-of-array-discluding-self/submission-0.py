class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prodList = [];
        for i in range(len(nums)):
            product = 1
            for x in range(len(nums)):
                if x == i:
                    continue
                product = product * nums[x]
            prodList.append(product)
        return prodList

