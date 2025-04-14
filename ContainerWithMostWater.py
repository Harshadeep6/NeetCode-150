from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1

        res = 0
        while left < right:
            area = (right - left) * min(heights[left], heights[right])

            res = max(res, area)

            if heights[left] >= heights[right]: right -= 1
            else: left += 1

        return res

if __name__ == '__main__':
    height=[0,2,0,3,1,0,1,3,2,1]
    print(Solution().maxArea(height))