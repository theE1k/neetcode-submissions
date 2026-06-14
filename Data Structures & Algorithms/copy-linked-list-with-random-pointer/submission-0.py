"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        storage = {None:None}
        curr = head
        while curr:
            storage[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            storage[curr].next = storage[curr.next]
            storage[curr].random = storage[curr.random]
            curr = curr.next
        return storage[head]