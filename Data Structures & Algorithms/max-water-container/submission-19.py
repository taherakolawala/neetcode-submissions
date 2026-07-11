class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L, R = 0, len(heights) - 1
        ret = min(heights[L], heights[R]) * (R-L)
        while L < R:
            if heights[L] <= heights[R]:
                L += 1
                ret = max(ret, min(heights[L], heights[R]) * (R-L))
            else:
                R -= 1
                ret = max(ret, min(heights[L], heights[R]) * (R-L))
        return ret
