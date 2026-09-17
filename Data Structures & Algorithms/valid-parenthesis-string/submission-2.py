class Solution:
    def checkValidString(self, s: str) -> bool:
        low = 0
        high = 0

        for i in range(len(s)):
            if s[i] == '(':
                low +=1
                high +=1
            if s[i] == ')':
                high -=1
                low = max(low-1,0)
            if s[i] == '*':
                low = max(0,low-1)
                high +=1
            if high < 0:
                return False
        return low == 0
            