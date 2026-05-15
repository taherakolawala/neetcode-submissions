class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # nums = set(nums)
        # starts = set()
        # ret = 0
        # for num in nums:
        #     if (num - 1) not in nums:
        #         starts.add(num)
        # for num in starts:
        #     i = num
        #     seq_len = 1
        #     while i + 1 in nums:
        #         seq_len += 1
        #         i = i+1
        #     if seq_len > ret:
        #         ret = seq_len
        # return ret
        
        nums = set(nums)
        ret = 0
        for num in nums:
            if (num - 1) not in nums:
                i = num
                seq_len = 1
                while i + 1 in nums:
                    seq_len += 1
                    i = i+1
                if seq_len > ret:
                    ret = seq_len
            else:
                continue
        return ret