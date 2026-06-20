class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}

        for i, num in enumerate(nums):
            if target - num in check.keys():
                return [check[target - num], i]
            check[num] = i
        
