class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        data_set = set(nums)
        max_length = 1
        for num in data_set:
            j = num + 1
            length = 1
            if num - 1 not in data_set: 
                while j in data_set:
                    j+=1
                    length +=1
            max_length = max(max_length, length)
        return max_length