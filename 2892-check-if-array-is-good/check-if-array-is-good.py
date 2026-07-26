class Solution:
    def isGood(self, nums: List[int]) -> bool:
        m=max(nums)
        freq=Counter(nums)
        for i in range(1,m):
            if freq[i]!=1: return False
        return freq[m] == 2

        