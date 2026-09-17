"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals: return 0
        heap = []

        intervals.sort(key=lambda x:x.start)
        heapq.heappush(heap, intervals[0].end)
        
        for i in intervals[1:]:
            min_value = heap[0]
            heapq.heappush(heap, i.end)
            if i.start >= min_value:
                heapq.heappop(heap)
                
        return len(heap)
