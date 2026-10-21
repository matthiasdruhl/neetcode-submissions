class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Start with initial
        # For each number we have to check if there is any combination of numbers before it that equals 2
        # either sliding window or prefix sum
        # Naive solution
        # Check very combination until you find one that works
        
        # Starting at first index keep array including that value
        # for each next item add it to the original value
        # iterate over the sub array at each point to check if it is equal to k
        
        # who have an array
        # Keep hash map of prefix sum and then for every item in array see if prefix - k is in array


        result = 0
        h = {0: 1}
        p = 0

        for i in range(len(nums)):
            p += nums[i]
            result += h.get(p - k, 0)
            h[p] = h.get(p, 0) + 1
        return result
        
            
        