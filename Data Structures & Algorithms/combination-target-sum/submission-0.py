class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        result = []

        def backtrack(start,current):
            total = sum(current)
            if total == target:
                result.append(current[:])
                return
            if total > target:
                return
            for i in range(start,len(nums)):
                current.append(nums[i])
                backtrack(i,current)
                current.pop()
        
        backtrack(0,[])
        return result

