class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        ans = 0

        for val in nums:
            if val - 1 not in numsSet:
                count = 0
                while (val + count) in numsSet:
                    count += 1
                ans = max(count, ans)
        return ans