class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights)-1
        maximum = lambda x,y :min(heights[x], heights[y]) * (y - x)
        current_max = maximum(left, right)
        while left<right:
            if heights[left] <= heights[right]:
                left += 1
                if current_max < maximum(left, right):
                    current_max = maximum(left, right)
            else :        
                right -= 1
                if current_max < maximum(left, right):
                        current_max = maximum(left, right)

        return current_max

            








        