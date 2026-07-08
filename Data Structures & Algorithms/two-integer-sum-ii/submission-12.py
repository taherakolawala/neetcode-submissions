class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ptr1, ptr2 = 0, len(numbers) - 1
        while ptr1 < ptr2:
            if numbers[ptr2] + numbers[ptr1] == target:
                return [ptr1+1, ptr2+1]
            if target - numbers[ptr2] <= numbers[ptr1]:
                ptr2 -= 1
                continue
            ptr1 += 1
            
            

