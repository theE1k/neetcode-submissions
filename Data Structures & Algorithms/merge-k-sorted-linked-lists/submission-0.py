# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        heap = []
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(heap,(head.val,i,head))
        dummy = ListNode(-1)
        p = dummy
        while heap:
            val,i,node = heapq.heappop(heap)
            if node.next:
                heapq.heappush(heap,(node.next.val,i,node.next))
            p.next = node
            p = p.next
        return dummy.next