class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # create a counter hashmap to count chars in t
        # iterate over s until we find a char that is in t
        # keep track of start point
        # have a counter to keep track of found chars
        # For every char in s track if char is in counter and if so decrement count
        # when counter reaches len(t) hold substring
        
        curr_string = ""
        shortest_string = s + 'a'
        c = Counter(t)
        found_char = 0
        l = 0
        r = 0
        
        while r < len(s) and s[r] not in c:
            r += 1
        if r == len(s):
            return ""
        found_char += 1
        c[s[r]] -= 1
        l = r
        r += 1

        

        if found_char == len(t):
            return s[r - 1]


        while r < len(s):
            if s[r] in c:
                
                c[s[r]] -= 1
                
                if c[s[r]] >= 0:
                    found_char += 1
                    
                if found_char == len(t):
                    if r - l < len(shortest_string):
                        if r < len(s) - 1:
                            shortest_string = s[l:r + 1]
                        else:
                            shortest_string = s[l:]
                    while found_char == len(t):
                        if s[l] in c:
                            
                            
                            if c[s[l]] <= 0:
                                if r - l < len(shortest_string):
                                    if r < len(s) - 1:
                                        shortest_string = s[l:r + 1]
                                    else:
                                        shortest_string = s[l:]
                            c[s[l]] += 1 
                            if c[s[l]] > 0:
                                found_char -= 1
                                l += 1
                                while s[l] not in c and s[l] != s[l - 1]:
                                    l += 1
                                    
                                break
                           
                                
                            

                        l += 1
            r += 1
        print(found_char, l)
        if len(shortest_string) > len(s):
            return ""
        return shortest_string
                        




