class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        b = len(nums)
        while i < b:
            if nums[i] == val:
                b -= 1
                nums[i], nums[b] = nums[b], nums[i]
            else:
                i += 1
        return b
         