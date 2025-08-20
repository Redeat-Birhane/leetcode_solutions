# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        dummy = ListNode(0)
        while head:
            curr = head.next
            head.next = prev
            prev = head
            head = curr
        dummy.next = prev
        return dummy.next
        