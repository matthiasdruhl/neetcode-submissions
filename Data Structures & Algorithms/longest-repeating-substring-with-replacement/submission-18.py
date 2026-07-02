class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Left pointer and right pointer
        # Hashmap to keep track of character count
        # Tracker keep track of largest character
        # slide right and add character to tracker
        # check if largest count is bigger then current char
        # if so update max
        # if max + k > r - l move on
        # else:
        #    remove l from counter
        #    slide l
        #       check if max > counter[l]
        #       check if max + k > r - l
    
        l = 0
        r = 1
        tracker = {s[l]: 1}
        longest = 1
        res = 0

        while r < len(s):
           
            if s[r] in tracker: 
                tracker[s[r]] = tracker[s[r]] + 1
            else:
                tracker[s[r]] = 1
            longest = max(longest, tracker[s[r]])

            if longest + k < (r - l + 1):
                

                tracker[s[l]] -= 1

                l += 1
            
            res = max(r - l + 1, res)
            r += 1
            print(r, l)
            
        return r - l
        
           