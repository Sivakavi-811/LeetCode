class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r,c = len(matrix),len(matrix[0])
        l,r = 0,(r*c)-1
        while l<=r:
            mid = l+(r-l)//2
            midrow = mid // c
            midcol = mid % c
            midval = matrix[midrow][midcol]
            if midval == target:
                return True
            elif midval < target:
                l  = mid + 1
            else:
                r = mid - 1
        return False
        