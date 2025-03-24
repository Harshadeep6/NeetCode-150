class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        theSet = set()

        for x in nums:
            if x in theSet:
                return True
            theSet.add(x)
        return False