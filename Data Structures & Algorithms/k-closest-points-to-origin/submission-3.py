class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def getEuclidean(x, y) -> int:
            return math.sqrt((x*x) + (y*y))


        minHeap = []
        point_map = {}
        for i in range(len(points)):
            x, y = points[i][0], points[i][1]
            euclidean = getEuclidean(x, y)
            
            if euclidean in point_map:
                temp = point_map[euclidean]
                temp.append([x,y])
                point_map[euclidean] = temp
            else:
                point_map[euclidean] = [[x, y]]
                heapq.heappush(minHeap, euclidean)
        
            print(point_map)
        ans = []
        while k > 0:
            low_euclidean = heapq.heappop(minHeap)
            print(low_euclidean)
            low_points = point_map[low_euclidean]
            for point in low_points:
                ans.append(point)
                k -= 1
                if k == 0:
                    return ans
        return ans