class Solution:
    def countBits(self, n: int) -> List[int]:
        
        # result = []
        # for i in range(n+1):
        #     count = bin(i).count('1')
        #     result.append(count)
        
        # return result

        offset = 1
        ans = [0] * (n+1)
        for i in range(1, n + 1):
            if i == offset * 2:
                offset = i
            ans[i] = ans[i - offset] + 1
        return ans