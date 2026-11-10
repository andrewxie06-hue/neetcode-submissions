# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        ahead = list1
        bhead = list2
        merged_head = None
        chosen = None
        merge = None
        while ahead is not None or bhead is not None:
            if ahead is None and bhead is not None:
                chosen = bhead
                bhead = bhead.next
            elif ahead is not None and bhead is None:
                chosen = ahead
                ahead = ahead.next
            elif ahead is not None and bhead is not None:
                if ahead.val > bhead.val:
                    chosen = bhead
                    bhead = bhead.next
                else:
                    chosen = ahead
                    ahead = ahead.next
            if merged_head is None:
                merged_head = chosen
                merge = chosen
            else:
                merge.next = chosen
                merge = merge.next
        return merged_head


            