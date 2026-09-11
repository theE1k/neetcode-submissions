class Solution:
    def longestPalindrome(self, s: str) -> str:

        sub_string = ''
        for i in range(len(s)):
            l = r = i
            while l >= 0 and r < len(s):
                if s[l] == s[r] and len(sub_string) < r-l + 1:
                    sub_string = s[l:r+1]
                elif s[l] != s[r]:
                    break
                l = l-1
                r = r+1
            l = i
            r = i+1
            while l >= 0 and r < len(s):
                if s[l] == s[r] and len(sub_string) < r-l + 1:
                    sub_string = s[l:r+1]
                elif s[l] != s[r]:
                    break
                l = l-1
                r = r+1
        return sub_string