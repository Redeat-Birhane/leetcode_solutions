# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr_node = dummy
        arr = []
        for linked_list in lists:
            while linked_list:
                arr.append(linked_list.val)
                linked_list = linked_list.next

        arr.sort()
        for li in arr:
            li = ListNode(li)
            curr_node.next = li
            curr_node = li
        return dummy.next

         