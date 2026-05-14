class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupset = set()
        for num in nums:
            if num not in dupset:
                dupset.add(num)
            else:
                return True
        return False