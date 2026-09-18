class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n <0:
            x = 1/x
            n = -n
    
        def recursive(x,n):
            if n == 0:
                return 1
            half = recursive(x,n//2)
            if n & 1:
                return half**2*x
            return half**2
        
        return recursive(x,n)
            