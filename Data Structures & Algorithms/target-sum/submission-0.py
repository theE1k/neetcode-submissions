class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sums = sum(nums)
        if target > sums or target < -sums:
            return 0
        dp = [[0] * (sums*2+1) for _ in range(len(nums)+1)]

        dp[0][sums] = 1
        

        for i in range(1,len(nums)+1):
            for j in range(sums*2+1):
                if j - nums[i-1] >= 0:
                    dp[i][j] = dp[i-1][j-nums[i-1]]
                if j + nums[i-1] <= 2*sums:
                    dp[i][j] += dp[i-1][j+nums[i-1]]


        return dp[len(nums)][target+sums]