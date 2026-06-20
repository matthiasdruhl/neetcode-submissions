class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = set(["+", "-", "*", "/"])

        for i in tokens:
            if i not in op:
                stack.append(i)
            else:
                if i == "+":
                    temp = int(stack.pop())
                    temp += int(stack.pop())
                    stack.append(temp)
                elif i == "*":
                    temp = int(stack.pop())
                    temp *= int(stack.pop())
                    stack.append(temp)
                elif i == "/":
                    temp = int(stack.pop())
                    zero_check = int(stack.pop())
                    if zero_check == 0:
                        temp = 0
                    else:
                        temp = zero_check / temp
                    
                    stack.append(temp)

                else:
                    temp = int(stack.pop())
                    temp = int(stack.pop()) - temp
                    stack.append(temp)
            
        return int(stack.pop())
                    