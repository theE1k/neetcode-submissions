class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        state = [0] * numCourses
        graph = defaultdict(list)
        for u,v in prerequisites:
            graph[v].append(u)
        result = []
        def dfs(node):
            if state[node] == 1:
                return False
            if state[node] == 2:
                return True
            state[node] = 1
            for i in graph[node]:
                if not dfs(i):
                    return False
            state[node] = 2
            result.append(node)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return result[::-1]