class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        x = []
        for i in range(0, len(nums)):
            if nums[i] in x:
                return True
            else:
                x.append(nums[i])
        return False
        