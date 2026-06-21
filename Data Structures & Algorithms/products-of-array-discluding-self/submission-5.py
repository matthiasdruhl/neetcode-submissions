class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Prefix sum
            # array starts with 1
            # each item is nums[i - 1] * pre[i - 1]
        
        
        # For each item in prefix multiply by postfix
        pre = [1] * len(nums)
    
        
       
        i = 1
        while i < len(nums):
            pre[i] = nums[i - 1] * pre[i - 1]
            i += 1

        post = nums[-1]
        i = len(nums) - 2
        while i >= 0:
           pre[i] = pre[i] * post
           post *= nums[i]
           i -= 1
        
        return pre
        
