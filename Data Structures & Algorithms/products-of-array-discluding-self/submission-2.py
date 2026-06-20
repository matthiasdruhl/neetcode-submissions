class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        pre = [1]

        for i in range(len(nums) - 1):
            pre.append(nums[i] * pre[i])

        postFix = nums[-1]
        for i in reversed(range(1, len(nums) - 1)):

            print(i)
            
            pre[i] = pre[i] * postFix
            postFix *= nums[i]

        pre[0] = postFix
        return pre
        
        
