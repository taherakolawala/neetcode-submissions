class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prodList = []
        prefix = []
        suffix = []
        product = 1

        for i in range(len(nums)):
            if i == 0:
                prefix.append(1)
                continue
            product *= nums[i-1]
            prefix.append(product)
        print(prefix)

        product = 1
        for g in range(len(nums)-1, -1, -1):
            if g == (len(nums)-1):
                suffix.append(1)
                continue
            product *= nums[g+1]
            suffix.append(product)
        suffix.reverse()
        print(suffix)

        for l in range(len(nums)):
            prodList.append(prefix[l]*suffix[l])
        
        return prodList

