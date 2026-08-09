class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:\

        import math
        import heapq
        def euc(x, y):
            return math.sqrt(x ** 2 + y ** 2)

        
        large = float('-inf')
        sol = []
        for p in points:

            e = euc(p[0], p[1])
            if len(sol) < k:
                heapq.heappush(sol, (-e, p))
                large = (sol[0])[0]

            else:
                if -e > large:
                    heapq.heappop(sol)
                    heapq.heappush(sol, (-e, p))
                    large = (sol[0])[0]
        
        
        ans = []
        for s in sol:
            ans.append(s[1])

        return ans
        

