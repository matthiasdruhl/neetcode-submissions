class Solution:
    def trap(self, height: List[int]) -> int:
        # two pointer
        # keep water count
        # Check left and right
        # Keep a left max and right max
        # When interating
            # if new level is lower add min - level to total water
            # if new level is higher or same, you can add current water to total water

        l = 0
        r = len(height) - 1
        total_water = 0
        l_max = height[l]
        r_max = height[r]

        while l < r:
            if l_max <= r_max:
                l += 1
                if height[l] < l_max:
                    total_water += l_max - height[l]
                else:
                    l_max = height[l]
            else:
                r -= 1
                if height[r] < r_max:
                    total_water += r_max - height[r]
                else:
                    r_max = height[r]
        return total_water

