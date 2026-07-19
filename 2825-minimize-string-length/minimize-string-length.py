class Solution:
    def minimizedStringLength(self, s: str) -> int:
        seen=[0]*26
        uni=0
        for c in s:
            t=ord(c)-ord('a')
            if seen[t] == 0:
                seen[t]=1
                uni+=1
        return uni
        