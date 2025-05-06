class Solution:
    def isValid(self, s: str) -> bool:
        mapp = {')': 1, ']': 2, '}': 2}
        stack = []
        for i in range(len(s)):
            if s[i] == ')' or s[i] == ']' or s[i] == '}':
                if stack:
                    if ord(stack.pop()) + mapp[s[i]] != ord(s[i]): return False
                else: return False
            else:
                stack.append(s[i])
        
        return not stack