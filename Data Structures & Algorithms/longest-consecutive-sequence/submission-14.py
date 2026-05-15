class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        starts = dict()
        for num in nums:
            if (num - 1) not in nums:
                starts[num] = 1
        for key in starts:
            i = key
            while i+ 1 in nums:
                starts[key] += 1
                i = i+1
        return max(starts.values(), default=0)
        