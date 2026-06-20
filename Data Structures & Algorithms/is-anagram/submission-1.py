class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        check1 = []
        for i in range(len(s)):
            check1.append(s[i])
        for o in range(len(t)):
            if t[o] in check1:
                check1.remove(t[o])
            else:
                return False

        return True

        