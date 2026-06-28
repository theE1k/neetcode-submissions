class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))
        minutes = 0
        while(queue):
            for _ in range(len(queue)):
                r,c = queue.popleft()
                for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nr,nc = dr+r,dc+c
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr,nc))
            if queue:
                minutes +=1
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:  # 还有新鲜橘子
                    return -1
        return minutes