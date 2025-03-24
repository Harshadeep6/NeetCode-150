class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        return "~".join(strs) + '~'

    def decode(self, s: str) -> List[str]:
        if s == "~":
            return [""]
        
        elif s == "":
            return []

        singleStr = ""
        res = []

        for i in range(len(s)):
            if s[i] == '~':
                res.append(singleStr)
                singleStr = ""
                continue
            
            singleStr += s[i]
        
        return res