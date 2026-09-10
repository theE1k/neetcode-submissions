class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
                return nums[0]
        def rob_lines(nums):
            if len(nums) == 1:
                return nums[0]
        
            prev1 = nums[0]
            prev2 = max(nums[0],nums[1])
            for i in range(2,len(nums)):
                curr = max(prev2,nums[i] + prev1)
                prev1 = prev2
                prev2 = curr
            return prev2
        return max(rob_lines(nums[:-1]),rob_lines(nums[1:]))