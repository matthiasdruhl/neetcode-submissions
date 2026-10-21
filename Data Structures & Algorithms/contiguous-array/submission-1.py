class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # Hashmap + prefix_sum
        # prefix = 0
        # iterate over array
            # if 1, add 1 to prefix
            # if 0, subtract 1
            # Check if prefix in map already
            # if so take max(res, map value)
            # else add prefix to map with index]
        r = 0
        h = {0: -1}
        p = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                p -= 1
            else:
                p += 1

            if p in h:
                r = max(r, i - h[p])
            else:
                h[p] = i
            
        return r
