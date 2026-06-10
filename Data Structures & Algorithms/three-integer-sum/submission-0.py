class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        output = []
        nums = sorted(nums)
        for i in range(0,len(nums)-2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            left = i+1
            right = len(nums)-1
            while left < right:
                total = nums[left] + nums[right]
                if total == target:
                    output.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total > target:
                    right -= 1
                else:
                    left += 1
        return output
