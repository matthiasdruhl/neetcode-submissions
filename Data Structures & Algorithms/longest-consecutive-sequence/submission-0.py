class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        longSeq = 0

        for num in nums:
            if num - 1 in numSet or num not in numSet:
                continue
            tempSeq = 1
            while num + 1 in numSet:
                numSet.remove(num)
                num = num + 1
                tempSeq += 1
            longSeq = max(tempSeq, longSeq)
        
        return longSeq