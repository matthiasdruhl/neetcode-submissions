class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        maxArea = 0

        while l < r:
            if heights[l] > heights[r]:
                base = heights[r] * (r - l)
                r -= 1
            else:
                base = heights[l] * (r - l)
                l += 1
            maxArea = max(maxArea, base)
        return maxArea