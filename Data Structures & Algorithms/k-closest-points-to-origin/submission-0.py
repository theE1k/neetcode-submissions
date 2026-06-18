class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []
        heap = [(x**2 + y**2, [x, y]) for x, y in points]
        heapq.heapify(heap)
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        return result