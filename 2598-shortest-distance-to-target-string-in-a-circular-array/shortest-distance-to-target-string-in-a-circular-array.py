class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n=len(words)
        min_dist=9999
        for i,word in enumerate(words):
            if word ==  target:
                right_dist=(i-startIndex+n)%n
                left_dist=(startIndex-i+n)%n
                min_dist=min(min_dist,right_dist,left_dist)
        return -1 if min_dist == 9999 else min_dist