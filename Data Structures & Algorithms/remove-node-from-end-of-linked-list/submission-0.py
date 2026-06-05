# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        totalNodes=0
        while curr:
            totalNodes+=1
            curr=curr.next
        i = (totalNodes-n)
        meow = curr = ListNode()
        curr.next=head
        while i>0:
            i-=1
            curr=curr.next
        curr.next=curr.next.next
        return meow.next


        