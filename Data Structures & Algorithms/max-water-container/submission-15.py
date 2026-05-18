class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L, R  = 0, len(heights) - 1
        ret = 0
        while L < R:
            area = (R - L) * (min(heights[R], heights[L]))
            if area > ret:
                ret = area
            if heights[R] < heights[L]:
                R -= 1
            elif heights[L] < heights[R]:
                L += 1
            else:
                L += 1
        return ret