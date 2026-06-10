class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        empty_map = {}
        for i in s:
            if i in empty_map:
                empty_map[i] += 1
            else:
                empty_map[i] = 1
        for i in t:
            if i in empty_map:
                if empty_map[i] - 1 == 0:
                    empty_map.pop(i)
                else:
                    empty_map[i] -= 1
            else:
                return False
        return not empty_map
