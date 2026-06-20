class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        check = {}
        for let in s:
            if let in check.keys():
                check[let] += 1
            else:
                check[let] = 1
        for let in t:
            if let not in check.keys() or check[let] == 0:
                return False
            else:
                check[let] -= 1
           
        return True


    

        