class Solution:
    def getSum(self, a: int, b: int) -> int:

        MASK = 0xFFFFFFFF
        while b != 0:
            sum_without_carry = (a ^ b) & MASK
            carry = ((a & b) << 1) & MASK
            a = sum_without_carry
            b = carry
        return a if a <= 0x7FFFFFFF else a - 0x100000000

