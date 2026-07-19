from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        row, col = len(grid), len(grid[0])
        visit = set()
        max_area = 0

        def bfs(r, c):
            q = deque()
            visit.add((r, c))
            q.append((r,c))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            island_area = 1

            while q:
                i, j = q.popleft()
                for dr, dc in directions:
                    nr, nc = i + dr, j + dc
                    if (nr in range(row) and
                        nc in range(col) and
                        grid[nr][nc] == 1 and
                        (nr, nc) not in visit):
                        q.append((nr, nc))
                        island_area += 1
                        visit.add((nr, nc))
            return island_area

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1 and (r, c) not in visit:
                    area = bfs(r, c)
                    max_area = max(area, max_area)
        return max_area