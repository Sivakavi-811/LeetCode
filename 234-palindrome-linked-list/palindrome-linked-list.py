# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        a=[]
        n=head

        while n is not None:
            a.append(n.val)
            n=n.next
        l,r=0,len(a)-1
        while l<r:
            if a[l] != a[r]:
                return False
            l+=1
            r-=1
        return True