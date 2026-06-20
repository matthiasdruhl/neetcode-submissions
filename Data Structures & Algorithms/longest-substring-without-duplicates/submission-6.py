class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        fast = 0
        slow = 0
        longSub = 0
        currLen = 0
        check = set()
        while fast < len(s):

            if s[fast] not in check:
                check.add(s[fast])
                currLen += 1
                fast += 1

            else:
                check.remove(s[slow])
                slow += 1
                longSub = max(longSub, currLen)
                currLen -= 1

        return max(longSub, currLen)
