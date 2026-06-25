class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        result = []
        open = 0
        close = 0

        def backtrack(current,open,close):
            if open == n and close == n:
                result.append(current)
                return
            if open < n:
                backtrack(current + '(', open + 1, close)
            if close < open:
                backtrack(current + ')', open, close + 1)

        
        backtrack("",open,close)
        return result
