class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        t = temperatures
        stack = [0]
        result = [0] * len(temperatures)
        for i in range(1, len(temperatures)):
            while stack:
                if t[i] > t[stack[-1]]:
                    j = stack.pop()
                    result[j] = i - j
                else:
                    break
            stack.append(i)
        return result
            
