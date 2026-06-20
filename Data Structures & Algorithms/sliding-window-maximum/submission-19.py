class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # When you iterate over the array you can assume if a value x is less then a value to the left and right of it in the array then you will mever use it

        # Keep heap
        # while iterating, if new max found, empty queue
        # else, if element > smallest element in queue, pop until element smallest in queue
        # else:
        # value doesn't matter
        # if left value 

        from collections import deque

        ans = []
        q = deque()
        q.append(nums[0])
       

        r = 1
        while r < k:
            if len(q) == 0:
                q.append(nums[r])

            elif nums[r] > q[-1]: 
                
                q.clear()
                q.append(nums[r])

            else:
                while len(q) > 0 and nums[r] > q[0]:
                    
                    q.popleft()
                q.appendleft(nums[r])
            r += 1
        ans.append(q[-1])
        


        

        while r < len(nums):
            
            if q[-1] == nums[r - k]:
                q.pop()

            if len(q) == 0:
                q.append(nums[r])

            elif nums[r] > q[-1]: 
                
                q.clear()
                q.append(nums[r])

            else:
                while len(q) > 0 and nums[r] > q[0]:
                    
                    q.popleft()
                q.appendleft(nums[r])
            ans.append(q[-1])
            r += 1

        return ans

        
