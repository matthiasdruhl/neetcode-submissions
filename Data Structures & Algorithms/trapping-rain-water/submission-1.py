class Solution:
    def trap(self, height: List[int]) -> int:
        # pointer at beginning and end
        # Keep reference to max on each side
        # Increment smaller side and update the max if needed
        # If smaller then max add diff to total

        rain_water = 0

        f = 0
        b = len(height) - 1

        left_high = height[f]
        right_high = height[b]
        


        while f < b:
            if height[f] < height[b]:
                f += 1
                if height[f] > left_high:
                    left_high = height[f]
                else:
                    rain_water += left_high - height[f]
            else:
                b -= 1
                if height[b] > right_high:
                    right_high = height[b]
                else:
                    rain_water += right_high - height[b]
        return rain_water


         

