class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-val for val in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            val1 = -heapq.heappop(heap)
            val2 = -heapq.heappop(heap)
            new_val = -(val1-val2)
            if new_val < 0:
                heapq.heappush(heap,new_val)
        return -heap[0] if heap else 0