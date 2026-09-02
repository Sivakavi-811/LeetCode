class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        res = []
        while(len(nums)>0):
            m1 = min(nums)
            m2 = max(nums)
            res.append((m1+m2)/2)
            nums.remove(m1)
            nums.remove(m2)
        return min(res)
        