class Solution:
    def trap(self, height: List[int]) -> int:
        heightLMax = []
        heightRMax = []
        res = 0
        for i in range(len(height)):
            res += min(max(height[:i+1]),max(height[i:]))-height[i]
        return res
