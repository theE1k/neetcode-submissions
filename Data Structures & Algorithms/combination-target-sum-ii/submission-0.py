class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result = []
        candidates.sort()

        def backtrack(start,current,total):
            if total == target:
                result.append(current[:])
                return
            pre = None
            for i in range(start,len(candidates)):
                if pre == candidates[i]:
                    continue
                if total > target:
                    break
                current.append(candidates[i])
                backtrack(i+1,current,total + candidates[i])
                current.pop()
                pre = candidates[i]
        
        backtrack(0,[],0)
        return result