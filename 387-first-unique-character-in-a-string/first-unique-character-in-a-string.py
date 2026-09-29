class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}
        # Count frequency of each character
        for char in s:
            freq[char] = 1 + freq.get(char, 0)
            
        # Iterate over the original string to find the first unique character index
        for i, char in enumerate(s):
            if freq[char] == 1:
                return i
                
        return -1
