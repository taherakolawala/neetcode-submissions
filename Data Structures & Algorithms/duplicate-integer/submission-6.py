class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            number = nums[i];
            for y in range(len(nums)):
                if y==i:
                    continue
                if number == nums[y]:
                    return True
        return False

