class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        if len(s) ==  1: return 1
        dup = set(s[0])
        max_len = 1 
        left = 0
        for right in range(1,len(s)):
            while s[right] in dup: 
                dup.remove(s[left])
                left+=1
            dup.add(s[right])
            max_len = max(max_len,len(dup))
        return max_len
        