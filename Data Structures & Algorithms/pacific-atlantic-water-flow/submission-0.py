class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows,cols = len(heights),len(heights[0])
        pacific = set()
        atlantic = set()
    

        result = []
        def dfs(r,c,visited, prev_height):
            if (r, c) in visited or r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if heights[r][c] < prev_height:
                return
            visited.add((r, c))
            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                dfs(r+dr, c+dc, visited, heights[r][c])


        # 从太平洋边界出发
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])      # 第一列
        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])      # 第一行
        
        # 从大西洋边界出发
        for r in range(rows):
            dfs(r, cols-1, atlantic, heights[r][cols-1])  # 最后一列
        for c in range(cols):
            dfs(rows-1, c, atlantic, heights[rows-1][c])  # 最后一行
        
        # 取交集
        return [[r, c] for r in range(rows) for c in range(cols) 
                if (r,c) in pacific and (r,c) in atlantic]