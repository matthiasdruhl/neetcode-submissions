class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Iterate over all numbers
        # Check if that number appears in the array before
        # Yes break
        # No move on to next number
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False