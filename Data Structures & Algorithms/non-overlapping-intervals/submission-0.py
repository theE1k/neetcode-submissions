class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        remove = 0

        intervals.sort()
        pre = intervals[0]
        for i in intervals[1:]:
            if pre[1] <= i[0]:
                pre = i
                continue
            else:
                remove += 1
                if pre[1] > i[1]:
                    pre = i
                    
        return remove