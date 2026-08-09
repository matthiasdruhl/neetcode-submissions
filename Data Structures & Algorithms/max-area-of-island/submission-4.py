class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_island = 0

        def dfs (grid, y, x):
            stack = []
            stack.append((y, x))
            island_size = 0
            grid[y][x] = 2

            while stack:
                curr = stack.pop()
                island_size += 1
                y = curr[0]
                x = curr[1]
                
                # check top

                if y > 0 and grid[y - 1][x] == 1:
                    stack.append((y - 1, x))
                    grid[y - 1][x] = 2
                

                # check bottom
                if y <  len(grid) - 1 and grid[y + 1][x] == 1:
                    stack.append((y + 1, x))
                    grid[y + 1][x] = 2
                    

                # check left

                if x > 0 and grid[y][x - 1] == 1:
                    stack.append((y, x - 1))
                    grid[y][x - 1] = 2
               
                
                if x < len(grid[0]) - 1 and grid[y][x + 1] == 1:
                    stack.append((y, x + 1))
                    grid[y][x + 1] = 2
                 

            
    
            
            return grid, island_size


        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 1:
                    grid[y][x] == 2
                    grid, island_size = dfs(grid, y, x)
                    max_island = max(max_island, island_size)

        return max_island
