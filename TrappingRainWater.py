class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        maxL, maxR = height[0], height[len(height) - 1]
        totalWater = 0

        while(left < right):
                if maxL <= maxR:
                        left += 1
                        if maxL - height[left] > 0:
                                totalWater += maxL - height[left]
                        maxL = max(height[left], maxL)
                else:
                        right -= 1
                        if maxR - height[right] > 0:
                                totalWater += maxR - height[right]
                        maxR = max(height[right], maxR)

        return totalWater