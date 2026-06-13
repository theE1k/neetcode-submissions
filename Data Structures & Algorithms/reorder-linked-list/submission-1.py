# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        pre = None
        while second:
            tmp = second.next
            second.next = pre
            pre = second
            second = tmp
        second = pre
        while second:
            tmp = head.next
            head.next = second
            second = second.next
            head.next.next = tmp
            head = tmp
        

        