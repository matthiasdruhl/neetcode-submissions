class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        
        l_high = heights[l]
        r_high = heights[r]
        max_area = ((r - l)) * min(l_high, r_high)
        


        while l < r:
            if l_high <= r_high:
                while l < r and heights[l] <= l_high:
                    l += 1
                l_high = heights[l]
            else:
                while l < r and heights[r] <= r_high:
                    r -= 1
                r_high = heights[r]

            max_area = max(max_area, ((r - l)) * min(l_high, r_high))

        return max_area

            