class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        

        result = []

        for i in range(len(intervals)):
            curr = intervals[i]

            # newInterval 完全在 curr 左边
            if newInterval[1] < curr[0]:
                result.append(newInterval)
                result.extend(intervals[i:])
                return result

            # newInterval 完全在 curr 右边
            elif newInterval[0] > curr[1]:
                result.append(curr)

            # 重叠
            else:
                newInterval[0] = min(newInterval[0], curr[0])
                newInterval[1] = max(newInterval[1], curr[1])

        result.append(newInterval)
        return result
                