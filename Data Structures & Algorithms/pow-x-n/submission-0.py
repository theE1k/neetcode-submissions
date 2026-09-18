class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        
        def recursive(x,n):
            if n == 0:
                return 1
            if n <0:
                x = 1/x
                n = -n
            if n & 1:
                return recursive(x*x,n//2) * x
            return recursive(x*x,n//2) 
        
        return recursive(x,n)
            