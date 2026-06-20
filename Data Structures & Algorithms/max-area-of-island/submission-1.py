class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        maxArea = 0

        def bfs(queue):
            area = 0
            while queue:
                curr = queue.popleft()
                area += 1
                
                for d in directions:
                    new = [curr[0] + d[0], curr[1] + d[1]]
                    if new[0] < 0 or new[0] >= rows or new[1] < 0 or new[1] >= cols:
                        continue
                    if grid[new[0]][new[1]] == 1:
                        grid[new[0]][new[1]] = 0
                        queue.append(new)
            return area
    

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    grid[r][c] = 0
                    queue.append([r,c])
                    maxArea = max(maxArea, bfs(queue))
        return maxArea
