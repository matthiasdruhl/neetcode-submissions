class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        check1 = []
        if len(s) != len(t):
            return False
        for let in s:
            check1.append(let)
        for let in t:
            if let not in check1:
                return False
            check1.remove(let)
        return True
