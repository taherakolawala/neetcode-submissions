class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupcheck = set(nums);
        if len(nums) == len(dupcheck):
            return False
        else:
            return True
    
        