class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        from collections import Counter
        count = Counter(nums)
        heap = []
        for key, val in count.items():
            heapq.heappush(heap, (-val, key))
        ans = []
        while len(ans) < k:
            ans.append(heapq.heappop(heap)[1])
        return ans







        


            
        

        
        
            



        