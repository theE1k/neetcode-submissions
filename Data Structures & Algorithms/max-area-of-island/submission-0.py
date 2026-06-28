class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid),len(grid[0])
        def dfs(r,c):
            if r <0 or r>=rows or c <0 or c >= cols or grid[r][c] != 1:
                return 0
            area = 1
            grid[r][c] = '#'
            area += dfs(r+1,c)
            area += dfs(r-1,c)
            area += dfs(r,c+1)
            area += dfs(r,c-1)
            return area
        count = 0 
        max_area = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    count += 1
                    area = dfs(r,c)
                    max_area = max(area,max_area)
        return max_area