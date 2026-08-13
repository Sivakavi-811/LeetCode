class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        #if row == 0:
        #    return -1
        col = len(grid[0])
        rot = deque()
        frsh = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    rot.append((i,j))
                elif grid[i][j] == 1:
                    frsh+=1
        mins = 0
        while rot and frsh > 0:
            mins+=1
            for i in range(len(rot)):
                x,y = rot.popleft()
                for dx,dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                    xx,yy = x+dx,y+dy
                    if xx<0 or xx == row or yy<0 or yy == col:
                        continue
                    if grid[xx][yy] == 0 or grid[xx][yy] == 2:
                        continue
                    frsh -= 1
                    grid[xx][yy] = 2
                    rot.append((xx,yy))
        return mins if frsh == 0 else -1
        