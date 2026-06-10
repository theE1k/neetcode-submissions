class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())
        # return s == s[::-1]
        return all(s[i] == s[~i] for i in range(len(s) // 2))
