class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        heap = [-c for c in freq.values()]
        heapq.heapify(heap)

        time = 0
        while heap:
            tmp = []
            for _ in range(n+1):
                if heap:
                    tmp.append(heapq.heappop(heap))
            for c in tmp:
                if c+1 <0:
                    heapq.heappush(heap, c + 1)
            if heap:
                time += n+1
            else:
                time += len(tmp)        
        
        return time
