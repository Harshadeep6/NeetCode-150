class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        sett = set()
        longest = 0

        for right in range(len(s)):
            while s[right] in sett:
                sett.remove(s[left])
                left += 1

            sett.add(s[right])
            longest = max(longest, right - left + 1)

        return longest