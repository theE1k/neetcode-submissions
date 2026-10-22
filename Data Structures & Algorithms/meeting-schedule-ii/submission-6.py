"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        res = count = i = j = 0
        begin = []
        end = []
        n = len(intervals)
        for interval in intervals:
            begin.append(interval.start)
            end.append(interval.end)
        begin.sort()
        end.sort()
        while i < n and j < n:
            if begin[i] < end[j]:
                count += 1
                res = max(res,count)
                i+=1
            else:
                count -= 1
                j+=1
        return res

