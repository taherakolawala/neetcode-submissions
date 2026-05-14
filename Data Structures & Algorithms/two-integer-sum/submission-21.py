class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        arrmap = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in arrmap:
                if arrmap[complement] > i:
                    return [i, arrmap[complement]]
                else:
                    return [arrmap[complement], i]
            
            arrmap[num] = i
            
        