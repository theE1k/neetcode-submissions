class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        empty_map = {}
        for i,num in enumerate(nums):
            num2 = target - num
            if num2 in empty_map:
                return [empty_map[num2],i]
            else:
                empty_map[num] = i
                
        