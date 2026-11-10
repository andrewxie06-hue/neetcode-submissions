class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        m = 0

        for i in range(len(heights) + 1):
            if i == len(heights):
                curr = 0
            else:
                curr = heights[i]

            while stack and heights[stack[-1]] > curr:
                height = heights[stack.pop()]

                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i

                m = max(m, height * width)

            stack.append(i)

        return m