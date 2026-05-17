class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ret = []
        for i in range(len(nums)):
            if i >= 1:
                if nums[i-1] == nums[i]:
                    continue
            j, k = i+1, len(nums) - 1
            while j < k:
                if j != i+1:
                    if nums[j] == nums[j-1]:
                        j += 1
                        continue
                if k != len(nums)-1:
                    if nums[k] == nums[k+1]:
                        k -= 1 
                        continue
                if (nums[i] + nums[j] + nums[k] == 0):
                    ret.append([nums[i], nums[j], nums[k]])
                    k -= 1
                    j += 1
                elif (nums[i] + nums[j] + nums[k] >= 0):
                    k -= 1
                elif (nums[i] + nums[j] + nums[k] <= 0):
                    j += 1 
        return ret 