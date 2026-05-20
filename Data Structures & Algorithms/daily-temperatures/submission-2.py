class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ret = []
        stk = []
        for i, temp in enumerate(temperatures):
            while stk and temp > stk[-1][0]:
                j = stk.pop()
                ret[j[1]] = i - j[1] 
            stk.append([temp, i])
            ret.append(0)         
        return ret
        