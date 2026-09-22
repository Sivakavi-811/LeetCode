class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        d={}
        for i,n in enumerate(nums):
            if n not in d:
                d[n]=[]
            d[n].append(i)
        mdist = 999999
        for ind in d.values():
            if len(ind)<3:
                continue
            for h in range(len(ind)-2):
                i = ind[h]
                j = ind[h+2]
                mdist = min(mdist, (j - i) * 2)
        return -1 if mdist == 999999 else mdist
        