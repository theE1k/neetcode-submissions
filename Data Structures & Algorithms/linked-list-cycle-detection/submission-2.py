# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow_node = head
        fast_node = head
        while fast_node:
            if not fast_node.next: return False
            fast_node = fast_node.next.next
            if not fast_node: return False
            slow_node = slow_node.next
            if slow_node == fast_node:
                return True
        return False
            