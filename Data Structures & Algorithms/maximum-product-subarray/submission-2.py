class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        pre_min = nums[0]
        pre_max = nums[0]
        res = nums[0]
        for i in range(1,len(nums)):
            dp_max = max(pre_max*nums[i],nums[i],pre_min*nums[i])
            res = max(res,dp_max)
            dp_min = min(pre_max*nums[i],nums[i],pre_min*nums[i])
            pre_max = dp_max
            pre_min = dp_min
        return res
        