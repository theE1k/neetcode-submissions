class Solution:
    def encode(self, strs: List[str]) -> str:
        encode = ""
        for string in strs:
            encode = encode + str(len(string)) + "#" + string
        return encode

    def decode(self, s: str) -> List[str]:
        decode = []
        i = 0
        while i < len(s):
            j = s.index('#',i)
            num = int(s[i:j])
            decode.append(s[j+1:j+ 1 + num])
            i = j + num +1
        return decode
