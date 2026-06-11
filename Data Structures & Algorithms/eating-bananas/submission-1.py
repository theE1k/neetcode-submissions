class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left,right = 1,max(piles)
        result = right

        while left <= right:
            mid = (right + left) // 2
            hour = 0
            for p in piles:
                hour += (p+mid-1)//mid
            
            if hour > h:
                left = mid + 1
            else:
                result = mid
                right = mid - 1
        return result

