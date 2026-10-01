class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        length = len(height)
        max_to_left = [0]*length
        max_to_right = [0]*length
        maximum = 0
        for i in range(length):
            if height[i] > maximum:
                maximum = height[i]
            max_to_left[i] = maximum
        maximum = 0
        for i in range(length-1, -1, -1):
            if height[i]>maximum:
                maximum = height[i]
            max_to_right[i] = maximum
        total = 0
        for i in range(length):
            total += min(max_to_left[i], max_to_right[i]) - height[i]
        return total
