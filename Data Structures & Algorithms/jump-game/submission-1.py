class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = nums[0]
        for i in range(1,len(nums)):
            if farthest < i:
                return False
            farthest = max(farthest,nums[i]+i)
            if farthest >= len(nums)-1:
                return True

        return farthest >= len(nums)-1