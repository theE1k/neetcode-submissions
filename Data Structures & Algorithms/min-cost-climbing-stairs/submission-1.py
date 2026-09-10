class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        memo = [-1] * len(cost)
        def dp(n):
            if n == 1:
                return cost[1]
            if n == 0:
                return cost[0]
            if memo[n] != -1:
                return memo[n]
            memo[n] = cost[n] + min(dp(n-1),dp(n-2))
            return memo[n]
        n = len(cost)
        return min(dp(n-2),dp(n-1))