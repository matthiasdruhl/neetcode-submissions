class MedianFinder:
    import heapq

    
     
    def __init__(self):
        # 2 heaps of equal size
        self.size = 0
        
        self.s = [] # max heap
        self.b = [] # min heap

    def rebalance(self):
        if len(self.s) - 1 > len(self.b):
            heapq.heappush(self.b, -heapq.heappop(self.s))
        elif len(self.b) - 1 > len(self.s):
            heapq.heappush(self.s, -heapq.heappop(self.b))

    def addNum(self, num: int) -> None:
        if len(self.s) == 0:
            self.s.append(-num)
        elif len(self.b) == 0:
            if num > -self.s[0]:
                self.b.append(num)
            else:
                self.b.append(-self.s[0])
                self.s[0] = -num

        else:
            if -num > self.s[0]:
                heapq.heappush(self.s, -num)
                self.rebalance()
                
            elif num > self.b[0]:
                heapq.heappush(self.b, num)
                self.rebalance()
            else:
                if len(self.s) > len(self.b):
                    heapq.heappush(self.b, num)
                else:
                    heapq.heappush(self.s, -num)
            

    def findMedian(self) -> float:
        
        if len(self.s) == len(self.b):
            return (-self.s[0] + self.b[0]) / 2

        print(self.s, self.b)
        return -self.s[0] if len(self.s) > len(self.b) else self.b[0]

        
        