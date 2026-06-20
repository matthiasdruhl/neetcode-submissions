class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        front = set(["[", "(", "{"])
       
        for i in s:
            if i in front:
                stack.append(i)
                
            else:
                if len(stack) == 0 or i == "]" and  stack[-1] != "[" or i == ")" and stack[-1] != "(" or i == "}" and stack[-1] != "{":
                    return False
                stack.pop()
        
        return len(stack) == 0
                