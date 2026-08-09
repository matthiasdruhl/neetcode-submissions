class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Instead of set use markers inside matrix
        # bfs over items 
        # How do I move from one island to the next
        # Iterate over i and j and check every i and j
        
        # y has to go first for indexing
        
        num_islands = 0

        def dfs (grid, y, x):
            stack = []
            stack.append((y, x))

            while stack:
                curr = stack.pop()
                y = curr[0]
                x = curr[1]

                # check top

                if y > 0 and grid[y - 1][x] == "1":
                    stack.append((y - 1, x))
                    grid[y - 1][x] = "X"

                # check bottom
                if y <  len(grid) - 1 and grid[y + 1][x] == "1":
                    stack.append((y + 1, x))
                    grid[y + 1][x] = "X"

                # check left

                if x > 0 and grid[y][x - 1] == "1":
                    stack.append((y, x - 1))
                    grid[y][x - 1] = "X"
                
                if x < len(grid[0]) - 1 and grid[y][x + 1] == "1":
                    stack.append((y, x + 1))
                    grid[y][x + 1] = "X"

            return grid


        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == "1":
                    dfs(grid, y, x)
                    num_islands += 1

        return num_islands


        



