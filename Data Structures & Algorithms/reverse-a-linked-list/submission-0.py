# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next != None and head.next.next:
            curr = head.next.next
            prev = head.next
            prev.next = head
            head.next = None
        elif head and head.next:
            _next = head.next
            head.next = None
            _next.next = head
            head = _next
            return head
        else:
            return head
            
            
        while curr.next:
            _next = curr.next
            curr.next = prev
            prev = curr
            curr = _next
        else:
            curr.next = prev
            head = curr

        return head



