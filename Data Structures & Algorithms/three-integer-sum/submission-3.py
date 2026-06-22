class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # return all triplets
        # indices should not be the same
        # iterate over indexes from 0
        # subtract nums[i] from target
        # run 2 sum on indexes i + 1 to end
        nums.sort()
        ans = []
        i = 0
        k = len(nums) - 1
        
        while i < len(nums) - 2:
            j = i + 1
            k = len(nums) - 1
            while j < k:
                temp = nums[i] + nums[k] + nums[j]
                if temp > 0:
                    k -= 1
                elif temp < 0:
                    j += 1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1  
            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1       

        return ans
                

