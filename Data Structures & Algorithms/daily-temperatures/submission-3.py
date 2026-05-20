class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ret = [0] * len(temperatures)
        stk = []
        for i, temp in enumerate(temperatures):
            while stk and temp > stk[-1][0]:
                j = stk.pop()
                ret[j[1]] = i - j[1] 
            stk.append([temp, i])      
        return ret
        