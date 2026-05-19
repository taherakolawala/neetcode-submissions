class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        ret = 0
        l, r = 0, len(height) - 1
        leftMar, rightMar = height[l], height[r]
        while l < r:
            if leftMar <= rightMar:
                l += 1
                leftMar = max(height[l], leftMar)
                ret += leftMar - height[l]
            else:
                r -= 1
                rightMar = max(height[r], rightMar)
                ret += rightMar - height[r]
        return ret

            
