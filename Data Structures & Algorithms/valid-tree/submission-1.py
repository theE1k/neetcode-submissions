class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = set()
        def dfs(node):
            visited.add(node)
            for i in graph[node]:
                if i not in visited:
                    dfs(i)
            

        dfs(0)
        return len(visited) == n
        