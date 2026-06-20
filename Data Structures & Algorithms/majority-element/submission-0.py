class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Use hashmap
        
        target = (len(nums) // 2) + 1
        counter = {}

        for num in nums:
            counter[num] = counter.get(num, 0) + 1
            if counter[num] == target:
                return num
