class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        maxCount = 0
        counts = [0] * 26
        res = 0

        for right, ch in enumerate(s):
            counts[ord(ch) - ord('A')] += 1

            maxCount = max(counts[ord(ch) - ord('A')], maxCount)

            if (right - left + 1) - maxCount > k:
                counts[ord(s[left]) - ord('A')] -= 1
                left += 1
            
            res = right - left + 1
        
        return res