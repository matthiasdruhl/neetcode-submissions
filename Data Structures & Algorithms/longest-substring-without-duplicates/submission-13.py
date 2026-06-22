class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        tracker = set()
        longest = 0 

        while r < len(s):
            
            if s[r] in tracker:
                longest = max(longest, r - l)
                
                while l < r:
                    if s[l] == s[r]:
                        l += 1
                        break
                    tracker.remove(s[l])
                    l += 1
            else:
                tracker.add(s[r])
            r += 1
        return max(longest, r - l)

       

        