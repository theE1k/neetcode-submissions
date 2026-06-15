class Node:
    def __init__(self,key=0,value=0):
        self.key = key
        self.value = value
        self.pre = None
        self.next = None

class LRUCache:

    

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.pre = self.head

    def insert(self,node: Node) -> None:
        node.pre = self.tail.pre
        node.next = self.tail
        self.tail.pre.next = node
        self.tail.pre = node
    
    def remove(self,node: Node) -> None:
        node.pre.next = node.next        
        node.next.pre = node.pre

    def get(self, key: int) -> int:
        node = self.cache.get(key)
        if not node:
            return -1
        self.remove(node)
        self.insert(node)
        return node.value
        
    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)
        if node:
            self.remove(node)
        node = Node(key,value)
        self.insert(node)
        self.cache[key] = node
        if len(self.cache) > self.capacity:
            lru = self.head.next
            self.remove(lru)
            del self.cache[lru.key]

        
