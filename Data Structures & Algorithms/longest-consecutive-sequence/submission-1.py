class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        curr = 1

        for num in numSet:
            if num - 1 in numSet:
                continue
            while num + 1 in numSet:
                curr += 1
                num = num + 1

            longest = max(longest, curr)
            curr = 1
        
        return longest