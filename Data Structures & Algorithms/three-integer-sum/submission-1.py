class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        ans = []
        nums = sorted(nums)
        

        

        for j in range(len(nums) - 1):
            
            if nums[j] > 0:
                break
            i = j + 1
            k = len(nums) - 1
            
            
            while i < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    if [nums[i], nums[j], nums[k]] not in ans:
                        ans.append([nums[i], nums[j], nums[k]])
                    
                        
                if nums[i] + nums[k] > (0 - nums[j]):
                    k -= 1
                
                else:
                    i += 1

        return ans
            
            