from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        row, col = len(grid), len(grid[0])
        fresh = 0
        q = deque()
        minutes = 0

        def bfs(q, minutes, fresh):
            direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            while q and fresh > 0:
                x = len(q)
                minutes += 1
                for i in range(x):
                    nc, nr = q.popleft()
                    for x,y in direction:
                        dc, dr = nc + x, nr + y
                        if (dc in range(row) and
                            dr in range(col) and
                            grid[dc][dr] == 1):
                            fresh -= 1
                            grid[dc][dr] = 2
                            q.append((dc, dr))
            return minutes, fresh

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))
        if fresh == 0:
            return 0
        minutes, fresh = bfs(q, minutes, fresh)
        if fresh != 0:
            return -1
        else:
            return minutes