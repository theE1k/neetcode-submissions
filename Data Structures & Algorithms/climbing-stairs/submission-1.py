class Solution:
    def climbStairs(self, n: int) -> int:
        
        mem = [-1] * (n+1)
        def dp(n):
            if n == 0 or n == 1:
                return 1
            if mem[n] != -1:
                return mem[n]
            result = dp(n-1) + dp(n-2)
            mem[n] = result
            return result
        
        return dp(n)