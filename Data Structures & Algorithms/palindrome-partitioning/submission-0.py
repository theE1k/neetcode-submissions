class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        result = []

        def is_palindramoe(word):
            left, right = 0, len(word) - 1
            while left < right:
                if word[left] != word[right]:
                    return False
                left +=1
                right -=1
            return True
            
        def backtrack(start,current):
            if start == len(s):
                result.append(current[:])
                return
            for end in range(start + 1, len(s) + 1):
                sub = s[start:end]
                if is_palindramoe(sub):
                    current.append(sub)
                    backtrack(end, current)
                    current.pop()

        backtrack(0,[])
        return result