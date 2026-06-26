class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        result = []
        def backtrack(start,current):
            if len(digits) == len(current):
                result.append(current)
                return
            s = phone[digits[start]]
            for c in s:
                backtrack(start+1,current+c)

        backtrack(0,"")
        return result 
