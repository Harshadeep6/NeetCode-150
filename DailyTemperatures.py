class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        
        for i, temp in enumerate(temperatures):
            if stack and temp > temperatures[i - 1]:
                while stack and stack[-1][0] < temp:
                    res[stack[-1][1]] = i - stack[-1][1]
                    stack.pop()
            stack.append([temp, i])

        return res