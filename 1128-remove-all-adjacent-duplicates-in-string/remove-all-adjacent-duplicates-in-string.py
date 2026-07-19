class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack=[]
        for j in s:
            if stack and j == stack[-1]:
                stack.pop()
            else:
                stack.append(j)
        return "".join(stack)



        