class Solution:
    def isPalindrome(self, s: str) -> bool:
        sCleaned = ""

        for char in s:
            if 65 <= ord(char) <= 90 or 97 <= ord(char) <= 122 or 48 <= ord(char) <= 57:
                if 65 <= ord(char) <= 90:
                    sCleaned += chr(ord(char) + 32)
                    continue
                sCleaned += char

        left, right = 0, len(sCleaned) - 1

        while(left <= right):
            if sCleaned[left] != sCleaned[right]:
                return False
            left += 1
            right -= 1
        
        return True