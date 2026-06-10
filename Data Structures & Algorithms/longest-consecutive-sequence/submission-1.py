class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        data_set = set()
        max_length = 1
        if len(nums) == 0:
            return 0
        for num in nums:
            data_set.add(num)
        for num in nums:
            j = num + 1
            length = 1
            if num - 1 not in data_set: 
                while j in data_set:
                    j+=1
                    length +=1
            if max_length < length:
                max_length = length
        return max_length