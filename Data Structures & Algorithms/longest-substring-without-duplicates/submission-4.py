class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dup = set()
        max_len = 0
        left = 0
        for right in range(len(s)):
            while s[right] in dup: 
                dup.remove(s[left])
                left+=1
            dup.add(s[right])
            max_len = max(max_len,len(dup))
        return max_len
        