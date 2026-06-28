class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        # 最小堆，(距离, 节点)
        heap = [(0, k)]
        visited = set()
        dist = {}  # 记录每个节点的最短距离
        while heap:
            d, node = heapq.heappop(heap)  # 取当前距离最短的
            if node in visited:
                continue
            visited.add(node)
            dist[node] = d
            
            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(heap, (d + weight, neighbor))
        
        if len(dist) == n:
            return max(dist.values())
        return -1