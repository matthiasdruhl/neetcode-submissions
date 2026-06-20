class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Return indices so we have to use hashmap
        
        check_map = {}

        for i in range(len(nums)):
            check_num = target - nums[i]
            if check_num in check_map:
                return [check_map[check_num], i]
            check_map[nums[i]] = i
                  

        
            


        