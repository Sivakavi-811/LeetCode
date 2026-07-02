class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward=[]
        res=[0]*len(nums)
        backward=[]
        res1=res2=1
        for i in range(len(nums)):
            forward.append(res1)
            res1*=nums[i]
            
        for i in range(len(nums)-1,-1,-1):
            backward.append(res2)
            res2*=nums[i]
        backward.reverse()
        for i in range(len(nums)):
            res[i] = forward[i] * backward[i]
        return res

        