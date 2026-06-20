class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check = []
        for i in nums:
            if i in check:
                return True
            check.append(i)
        return False 