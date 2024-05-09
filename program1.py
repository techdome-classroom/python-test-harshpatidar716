class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
       def dfs(row, col):
        # Check if the current cell is out of bounds or water
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == 'W':
             return
        # Mark the current cell as visited
            grid[row][col] = 'W'
        # Explore adjacent landmasses
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        num_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 'L':
                # Start DFS from an unvisited landmass
                    dfs(i, j)
                    num_islands += 1

        return num_islands

    #    write your code here
              
        return 0
