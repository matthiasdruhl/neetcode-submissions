class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Cast nums to set
        # iterate over set
        # if nums - 1 in set continue.
        
        nums = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in nums:
                curr_len = 1
                while num + 1 in nums:
                    curr_len += 1
                    num = num + 1
                longest = max(curr_len, longest)

        return longest