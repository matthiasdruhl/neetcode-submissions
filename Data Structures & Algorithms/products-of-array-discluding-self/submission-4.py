class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Prefix sum
            # array starts with 1
            # each item is nums[i - 1] * pre[i - 1]
        # postfix sum
            # iterate backwards over array
            # add to back of array
            # last item is 0
            # second to last item is nums[-1]
        
        # For each item in prefix multiply by postfix
        pre = [1] * len(nums)
        post = [1] * len(nums)
        ans = []
       
        i = 1
        while i < len(nums):
            pre[i] = nums[i - 1] * pre[i - 1]
            i += 1


        i = len(nums) - 2
        while i >= 0:
            post[i] = nums[i + 1] * post[i + 1]
            i -= 1
        
        i = 0
        while i < len(nums):
            ans.append(pre[i] * post[i])
            i += 1
            
            
      
        return ans
        
