class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res=""
        m=min(len(word1),len(word2))
        for i in range(m):
                res+=word1[i]
                res+=word2[i]
        res+=word1[m:]+word2[m:]
        return res


        