from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = Counter(hand)
        heap = [-x for x in count.keys()]
        heapq.heapify(heap)
        while count:
            value = -heap[0]
            for i in range(groupSize):
                curr = value - i
                if count[curr] == 0:
                    return False
                count[curr] -= 1
                if count[curr] == 0:
                    if curr != -heap[0]:
                        return False

                    heapq.heappop(heap)
                    del count[curr]

            
        return True



