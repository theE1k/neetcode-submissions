class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0: return False
        target = sum(nums) // 2

        dp = [False] * (target+1)
        dp[0] = True

        for i in nums:
            for s in range(target,i-1,-1):
                if dp[s-i] == True:
                    dp[s] = True

        
        return dp[target]
