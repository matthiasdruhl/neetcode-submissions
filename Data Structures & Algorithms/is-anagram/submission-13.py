class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        buckets = {}
        if len(s) != len(t):
            return False
        for char in s:
            if char not in buckets:
                buckets[char] = 1
            else:
                buckets[char] = buckets[char] + 1
        
        for c in t:
            if c not in buckets or buckets[c] == 0:
                return False
            buckets[c] = buckets[c] - 1

        return True
            
        