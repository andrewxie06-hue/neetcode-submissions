# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        k = head
    
        for i in range(n):
            k = k.next
        if k is None:
            head = head.next
            return head
        j = ListNode(0, head)
        while k is not None:
            k = k.next
            j = j.next
        j.next = j.next.next
        return head
      