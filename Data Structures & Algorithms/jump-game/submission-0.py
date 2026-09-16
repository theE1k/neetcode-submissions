class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 0: return True
        farthest = nums[0]
        for i in range(1,len(nums)):
            if farthest < i:
                return False
            farthest = max(farthest,nums[i]+i)

        return farthest >= len(nums)-1