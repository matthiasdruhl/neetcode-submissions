class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq

        h = []
        kl = float("-inf")

        for n in nums:
            if len(h) < k: 
                heapq.heappush(h, n)
                kl = h[0]
            
            else:
                if n > kl:
                    heapq.heappop(h)
                    heapq.heappush(h, n)
                    kl = h[0]

            
        
        return kl
