class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        remove = 0

        intervals.sort()
        pre_end = intervals[0][1]
        for i in intervals[1:]:
            if pre_end <= i[0]:
                pre_end = i[1]
            else:
                remove += 1
                if pre_end > i[1]:
                    pre_end = i[1]
                    
        return remove