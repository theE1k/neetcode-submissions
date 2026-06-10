class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        zero_count = 0
        for num in nums:
            if num != 0:
                total *= num
            else:
                zero_count += 1
        output = []
        if zero_count > 1:
            output = [0 for _ in nums]
            return output
        for num in nums:
            if num != 0 and zero_count == 1:
                output.append(0)
            elif num != 0:
                output.append(total//num)
            else:
                output.append(total)
        return output
        