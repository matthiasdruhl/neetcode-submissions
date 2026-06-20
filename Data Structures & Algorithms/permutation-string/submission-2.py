class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        buckets1 = [0] * 26
        buckets2 = [0] * 26
        f, b = 0, 0
        while b < len(s1):
            buckets1[ord(s1[b]) - ord("a")] += 1
            buckets2[ord(s2[b]) - ord("a")] += 1
            b += 1
        while b < len(s2):
            if buckets1 == buckets2:
                return True
            buckets2[ord(s2[b]) - ord("a")] += 1
            buckets2[ord(s2[f]) - ord("a")] -= 1
            f += 1
            b += 1
        if buckets1 == buckets2:
            return True
        return False

        
            
        
        

