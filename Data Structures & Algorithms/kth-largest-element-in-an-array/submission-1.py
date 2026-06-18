class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-val for val in nums]
        heapq.heapify(heap)
        for _ in range(k-1):
            heapq.heappop(heap)
        return -heap[0]
        
        
        