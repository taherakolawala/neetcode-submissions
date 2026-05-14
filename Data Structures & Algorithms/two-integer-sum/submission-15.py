class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        nums_dict =  dict()
        for i in range(0, len(nums)):
            if nums[i] in nums_dict:
                return [nums_dict[nums[i]], i]
            nums_dict[target - nums[i]] = i


        # nums_dict = dict()
        # for i in range(0, len(nums)):
        #     nums_dict[nums[i]] = i
        # for x in range(0, len(nums)):
        #     if target - nums[x] in nums_dict and x != nums_dict[target-nums[x]]:
        #         return [x, nums_dict[target-nums[x]]]
        #     else:
        #         pass
    
        # for x in range(len(nums)):
        #     for y in range(x,len(nums)):
        #         if x != y:
        #             if nums[x] + nums[y] == target:
        #                 return [x, y]
           
            
        