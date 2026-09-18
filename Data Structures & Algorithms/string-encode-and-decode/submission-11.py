class Solution:

    def encode(self, strs: List[str]) -> str:
        string = []
        for s in strs:
            string.append(str(len(s)))
            string.append('#')
            string.append(s)      
        return ''.join(string)


    def decode(self, s: str) -> List[str]:
        res = []
        length = len(s)
        width = ''
        i = 0
        while i < length:
            if s[i] != '#':
                width += s[i]
                i += 1
            else:
                width = int(width)
                res.append(s[i+1: i+width+1])
                i = i+width+1
                width = ''
        return res


