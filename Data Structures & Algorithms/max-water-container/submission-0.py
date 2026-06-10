class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left = 0
        right = len(heights)-1
        max_container = 0
        while left < right:
            left_height = heights[left]
            right_height = heights[right]
            min_height = min(left_height,right_height)
            container = min_height*(right-left)
            max_container = max(max_container,container)
            if left_height < right_height:
                left += 1
            else:
                right -= 1
        return max_container