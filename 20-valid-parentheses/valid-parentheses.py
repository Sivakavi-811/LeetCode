class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        bmap={')':'(','}':'{',']':'['}
        for i in range(len(s)):
            char=s[i]
            if char in bmap:
                if not stack:
                    return False
                if stack[-1]!=bmap[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        return len(stack) == 0