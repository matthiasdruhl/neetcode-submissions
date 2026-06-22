class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two pointer
        # check if l + r == target:
            # if so return
            # if > shift r
            # if < shift l

        l = 0
        r = len(numbers) - 1
        while l <= r:
            if numbers[r] + numbers[l] == target:
                return [l + 1, r + 1]
            
            elif numbers[r] + numbers[l] > target:
                r -= 1
            
            else:
                l += 1