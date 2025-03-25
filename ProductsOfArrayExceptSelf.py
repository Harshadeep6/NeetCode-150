class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)

        backFactorial = 1

        res[0] = 1
        for i in range(len(nums) - 1):
            res[i + 1] = nums[i] * res[i]
        
        for i in range(len(nums) - 2, -1, -1):
            backFactorial *= nums[i + 1]
            res[i] *= backFactorial

        return res