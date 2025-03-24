from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
            
        sCounter = Counter(s)
        tCounter = Counter(t)

        for letter in s:
            if sCounter[letter] != tCounter[letter]:
                return False

        return True