class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c for c in s if c.isalnum()).lower()
        palindrome_tuple = tuple(s)
        revert_s = ''
        for i in range(len(palindrome_tuple)-1,-1,-1):
            revert_s += palindrome_tuple[i]
        if revert_s == s:
            return True
        return False
