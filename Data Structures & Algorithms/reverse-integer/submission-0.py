class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0 :
            sign = -1
            x = -x
        
        result = 0

        MAX = 2**31-1
        MAX_digit = MAX%10
        MAX //= 10
        while x:
            digit = x%10
            x //= 10
            if result > MAX or result == MAX and (digit > MAX_digit
            or digit > MAX_digit+1 and sign == -1):
                return 0
            result = result *10 + digit
        
        return result * sign