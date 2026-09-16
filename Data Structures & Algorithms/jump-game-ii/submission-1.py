class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        count = 0
        farthest = nums[0]
        current_end = 0

        for i in range(len(nums)):
            farthest = max(farthest,nums[i]+i)
            if i == current_end:
                count +=1
                current_end = farthest
                if current_end >= len(nums) - 1:
                    return count
            
           

