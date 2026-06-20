class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # inputs:
            # grid: n * m grid consisting of 1 and 0

        # output:
            # number of islands
        
        # find all connected graphs
        # bfs


        rows = len(grid)
        cols = len(grid[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        num_islands = 0
        queue = deque()

        def bfs(queue):
            
            while queue:
                
                curr = queue.popleft()
                grid[curr[0]][curr[1]] = 0
                print(grid)
                
                for d in directions:
                    new_spot = [curr[0] + d[0], curr[1] + d[1]]
                    if new_spot[0] < 0 or new_spot[0] >= rows or new_spot[1] >= cols or new_spot[1] < 0:
                        continue
                    
                    if grid[new_spot[0]][new_spot[1]] == "1":
                        queue.append(new_spot)

                
        
        for r in range((rows)):
            for c in range((cols)):

                if grid[r][c] == "1":
                    print("NEW")
                    queue.append([r,c])
                    bfs(queue)
                    num_islands += 1
        return num_islands
            
        


            
        