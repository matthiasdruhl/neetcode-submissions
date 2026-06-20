class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Naive solution
        # Iterate over all bars
        #   for each bar find the max area for each bar where that bar is start
        
        # Naive solution
        max_area = 0
        for i in range(len(heights)):
            curr_area = heights[i]
            curr_min = heights[i]
            for o in range(i + 1, len(heights)):
                curr_min = min(curr_min, heights[o])
                curr_area = max(curr_area, curr_min * ((o - i) + 1))
            
            
            max_area = max(curr_area, max_area)
            

        return max(max_area, heights[-1])