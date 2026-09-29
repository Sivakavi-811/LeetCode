class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq={}
        for i in s:
            freq[i]=1+freq.get(i,0)
        for i,c in enumerate(s):
            if freq[c] == 1:
                return i
        return -1



        