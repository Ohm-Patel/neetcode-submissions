class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()

        directions = [[-1,0], [1,0], [0,-1], [0,1]]

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 0:
                    q.append([x,y])

        while q:
            coord = q.popleft()
            x = coord[0]
            y = coord[1]

            for dx,dy in directions:
                nx = x + dx
                ny = y + dy

                if nx < 0 or ny < 0 or nx >= len(grid[0]) or ny >= len(grid) or grid[ny][nx] != 2147483647:
                    continue

                grid[ny][nx] = grid[y][x] + 1
                q.append([nx,ny])


        