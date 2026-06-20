class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Keep hashmap referring to the characters that our window covers
        # variable to keep track of longest_substring
        # fast and slow pointer to reference front and end of window
        # Iterate over s
        # check if hashmap[s] + k < fast - slow
        # If yes:
        #   remove back of window from hashmap until hashmap[slow] + k == fast - slow
        # Since we have a window we can assume that it is the max window so we can also increment front

        check = {}

        char_max = 0
        l = 0
        res = 0

        for i in range(len(s)):
            check[s[i]] = check.get(s[i], 0) + 1
            char_max = max(check[s[i]], char_max) 
            while char_max + k < (i - l + 1):
                check[s[l]] -= 1
                l += 1
            res = max(res, i - l + 1)
        return res

        
            
                

        
        
                
            

            