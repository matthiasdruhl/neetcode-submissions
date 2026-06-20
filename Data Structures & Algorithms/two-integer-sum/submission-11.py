class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = {}
        for i in range(len(nums)):
            goal = target - nums[i]
            if goal in ans:
                return [ans[goal], i]
            ans[nums[i]] =i
            


        