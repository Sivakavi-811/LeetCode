class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        l=[]
        count=0
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if j!=i and nums[j]<nums[i]:
                    count+=1
            l.append(count)
            count=0
        return l

