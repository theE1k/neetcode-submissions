class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        result = [intervals[0]]
        for curr in intervals[1:]:
            last = result[-1]
            if curr[0] > last[-1]:
                result.append(curr)
            else:
                last[1] = max(last[1],curr[1])
        return result