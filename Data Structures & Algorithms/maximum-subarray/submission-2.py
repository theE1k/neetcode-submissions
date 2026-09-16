class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # if len(nums) == 1:
            # return nums[0]
        max_amount = nums[0]
        curr = nums[0]

        for i in range(1,len(nums)):
            if curr + nums[i] < nums[i]:
                curr = nums[i]
            else:
                curr += nums[i]
            max_amount = max(max_amount,curr)
        
        return max_amount