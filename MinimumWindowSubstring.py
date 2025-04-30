class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""
        
        sMap, tMap = {}, {}
        for i in range(len(t)):
            tMap[t[i]] = 1 + tMap.get(t[i], 0)
        
        res, resLen = [-1, -1], float('infinity')
        have, need = 0, len(tMap)
        l = 0
        for r in range(len(s)):
            sMap[s[r]] = 1 + sMap.get(s[r], 0)
            
            if s[r] in tMap and sMap[s[r]] == tMap[s[r]]:
                have += 1
                
            while have == need:
                if r - l + 1 < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                    
                sMap[s[l]] -= 1
                if s[l] in tMap and sMap[s[l]] < tMap[s[l]]:
                    have -= 1
                    
                l += 1
        
        l, r = res
        return s[l:r+1] if resLen != float('infinity') else ""