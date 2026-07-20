class Solution:
    def hIndex(self, c: List[int]) -> int:
        n=len(c)
        c.sort()
        for i,v in enumerate(c):
            if n-i<=v:
                return n-i
        return 0
        