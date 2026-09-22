class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        d={}
        for i,num in enumerate(nums):
            if num not in d:
                d[num]=[]
            d[num].append(i)
        mdist = 9999999999
        for ind in d.values():
            if(len(ind))<3:
                continue
            for h in range(len(ind)-2):
                i=ind[h]
                j=ind[h+2]
                mdist = min(mdist,(j-i)*2)
        return -1 if mdist == 9999999999 else mdist