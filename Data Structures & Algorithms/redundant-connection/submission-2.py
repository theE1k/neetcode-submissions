class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        n = len(edges)
        parent = [i for i in range(n + 1)]

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]  # 路径压缩
                x = parent[x]
            return x

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False  # 已经连通，有环
            parent[px] = py
            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]

        return []
