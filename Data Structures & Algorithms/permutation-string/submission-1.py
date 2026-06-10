class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s2) < len(s1): return False 
        s1_map = {}
        s2_map = {}
        length = len(s1)
        for i in range(len(s1)):
            s1_map[s1[i]] = s1_map.get(s1[i],0) + 1
            s2_map[s2[i]] = s2_map.get(s2[i],0) + 1
        pre_c = s2[0]
        for right in range(len(s1),len(s2)):            
            if s1_map == s2_map:
                return True
            else:
                s2_map[s2[right]] = s2_map.get(s2[right],0) + 1
                count = s2_map.get(pre_c,0) - 1
                if count == 0: s2_map.pop(pre_c)
                else: s2_map[pre_c] = count
                pre_c = s2[right-len(s1)+1]
        
        return s1_map == s2_map
        