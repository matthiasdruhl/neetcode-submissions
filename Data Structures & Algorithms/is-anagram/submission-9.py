class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        buckets = [0] * 52
        for char in s:
            buckets[ord(char) - ord('a')] += 1
        for char in t:
            if buckets[ord(char) - ord('a')] == 0:
                return False
            buckets[ord(char) - ord('a')] -= 1
            

           
        return True


    

        