from collections import Counter
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        f=Counter()
        max_len = 0
        l=0
        for r in range(len(nums)):
            f[nums[r]]+=1
            while f[nums[r]]>k:
                f[nums[l]]-=1
                l+=1
            size=r-l+1
            if size>max_len:
                max_len = size
        return max_len
