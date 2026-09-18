class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0 :
            sign = -1
            x = -x
        
        result = 0

        MAX = 2**31-1
        MAX_digit = MAX%10 if sign ==1 else MAX%10+1
        MAX //= 10
        while x:
            digit = x%10
            x //= 10
            if result > MAX or result == MAX and digit > MAX_digit:
                return 0
            result = result *10 + digit
        
        return result * sign