class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        init_map = {}
        for str in strs:
            new = tuple(sorted(str))
            if new in init_map:
                init_map[new].append(str)
            else:
                init_map[new] = [str]
        return list(init_map.values())