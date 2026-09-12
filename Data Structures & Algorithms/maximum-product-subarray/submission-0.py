class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp_min = [float('inf')] * len(nums)
        dp_max = [float('-inf')] * len(nums)

        dp_min[0] = nums[0]
        dp_max[0] = nums[0]
        res = nums[0]
        for i in range(1,len(nums)):
            dp_max[i] = max(dp_max[i-1]*nums[i],nums[i],dp_min[i-1]*nums[i])
            res = max(res,dp_max[i])
            dp_min[i] = min(dp_max[i-1]*nums[i],nums[i],dp_min[i-1]*nums[i])

        return res
        