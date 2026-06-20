class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest_consequtive = 0
        for num in seen:
            if num - 1 not in seen:
                curr_length = 1
                while num + 1 in seen:
                    curr_length += 1
                    num += 1
                longest_consequtive = max(longest_consequtive, curr_length)
        return longest_consequtive