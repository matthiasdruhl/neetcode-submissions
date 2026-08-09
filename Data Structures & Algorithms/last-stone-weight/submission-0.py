class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq

        sh = [-abs(x) for x in stones]
        heapq.heapify(sh)
      
        c = heapq.heappop(sh)

        while sh:
            n = heapq.heappop(sh)
            if c != n:
                
                heapq.heappush(sh, c - n)
            c = 0 if len(sh) == 0 else heapq.heappop(sh)

        return abs(c)
        
        
