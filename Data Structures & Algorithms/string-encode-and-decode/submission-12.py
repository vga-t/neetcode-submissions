class Solution:

    def encode(self, strs: List[str]) -> str:
        string = []
        for s in strs:
            string.append(str(len(s)))
            string.append('#')
            string.append(s)      
        return ''.join(string)


    def decode(self, s: str) -> List[str]:
        length = len(s)
        res = []
        i = 0
        while i < length:
            j = i
            while s[j]!='#':
                j = j+1
            width = int(s[i:j])
            res.append(s[j+1:j+width+1])
            i = j+width+1

        return res


            
            


