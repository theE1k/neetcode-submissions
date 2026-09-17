"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        
        if len(intervals) == 0:
            return True
        intervals.sort(key=lambda x: x.start)
        pre = intervals[0]
        for curr in intervals[1:]:
            if pre.end > curr.start:
                return False
            else:
                pre.end = curr.end

        return True