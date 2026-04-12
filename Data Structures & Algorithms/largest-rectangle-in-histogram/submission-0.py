class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        area = 0

        for idx in range(len(heights)):
            while stack and heights[idx] < heights[stack[-1]]:
                h = heights[stack.pop()]

                if not stack:
                    w = idx
                else:
                    w = idx - stack[-1] - 1
                

                area = max(h * w, area)

            stack.append(idx)

        n = len(heights)
        while stack:
            h = heights[stack.pop()]

            if not stack:
                w = n
            else:
                w = n - stack[-1] - 1

            area = max(area, h * w)

        return area