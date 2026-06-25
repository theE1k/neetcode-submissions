class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()


        def backtrack(start,current):
            result.append(current[:])
            pre = None
            for i in range(start,len(nums)):
                if pre == nums[i]:
                    continue
                current.append(nums[i])
                backtrack(i+1,current)
                current.pop()
                pre = nums[i]


        backtrack(0,[])
        return result