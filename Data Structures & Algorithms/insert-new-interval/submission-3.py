class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        start = newInterval[0]
        end = newInterval[1]

        result= []

        for i in range(len(intervals)):
            curr = intervals[i]
            if curr[0] > end:
                result.append([start,end])
                result.extend(intervals[i:])
                return result
            if curr[1] < start:
                result.append(curr)
                continue
            if curr[0] < start:
                start = curr[0]
            if curr[1] > end:
                end = curr[1]
        
        result.append([start,end])
        return result
                