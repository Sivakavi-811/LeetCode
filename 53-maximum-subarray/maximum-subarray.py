class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        st=end=nums[0]
        for i in range(1,len(nums)):
            end=max(nums[i],end+nums[i])
            st=max(st,end)
        return st

        