from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def bfs(i, j):
            q = deque()
            q.append((i, j))
            visit.add((i, j))

            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

            while q:
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (
                        nr in range(rows)
                        and nc in range(cols)
                        and (nr, nc) not in visit
                        and grid[nr][nc] == "1"
                    ):
                        q.append((nr, nc))
                        visit.add((nr, nc))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visit:
                    bfs(i, j)
                    islands += 1

        return islands