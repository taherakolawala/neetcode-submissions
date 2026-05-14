class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        x = dict()
        for i in range(0, len(nums)):
            if nums[i] in x:
                return True
            else:
                x[nums[i]] = 1
        return False
        