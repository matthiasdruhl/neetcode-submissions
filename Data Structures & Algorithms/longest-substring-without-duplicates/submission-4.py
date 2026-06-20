class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0

        hold = set()
        sub = 0

        while j < len(s):
            if s[j] in hold:
                hold.remove(s[i])
                sub = max(sub, j - i)
                
                i += 1
            else:
                hold.add(s[j])
                j += 1
        return max(sub, j - i)
