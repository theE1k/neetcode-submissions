class Solution:
    def isHappy(self, n: int) -> bool:

        result = set()
        while True:
            sums = 0
            while n != 0:
                digit = n % 10
                n //= 10
                sums += digit**2
            n = sums
            if sums == 1:
                return True
            if sums in result:
                return False
            else:
                result.add(sums)
            
        