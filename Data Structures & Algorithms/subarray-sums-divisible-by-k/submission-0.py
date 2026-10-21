class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        p = 0
        h = {0: 1}
        r = 0

        for i in range(len(nums)):
            p += nums[i]

            t = p % k
            r += h.get(t, 0)
            h[t] = h.get(t, 0) + 1

        return r