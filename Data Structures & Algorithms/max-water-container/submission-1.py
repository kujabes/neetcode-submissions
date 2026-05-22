class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        p1 = 0
        p2 = len(heights) - 1

        while p1 < p2:
            width = p2 - p1
            height = min(heights[p1], heights[p2])
            max_area = max(max_area, width * height)

            if heights[p1] < heights[p2]:
                p1 += 1
            else:
                p2 -= 1
            
        return max_area



