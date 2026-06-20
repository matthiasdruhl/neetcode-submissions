class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = {}
        for i in range(len(nums)):
            if target - nums[i] not in ans.keys():
                ans[nums[i]] = i
            else:
                return [ans[target - nums[i]], i]
            

        
            


        