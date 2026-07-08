class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums=[abs(n) for n in nums ]
        nums.sort()
        l=[]
        for i in nums:
            l.append(i*i)
        return l
        