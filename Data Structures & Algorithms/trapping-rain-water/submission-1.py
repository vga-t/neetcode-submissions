class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        max_to_left = []
        max_to_right = []
        maximum = 0
        for h in height:
            if h > maximum:
                maximum = h
            max_to_left.append(maximum)
        maximum = 0
        for i in range(len(height)-1, -1, -1):
            if height[i]>maximum:
                maximum = height[i]
            max_to_right.append(maximum)
        total = 0
        for i in range(len(height)):
            total = total + min(max_to_left[i], max_to_right[len(height)-1- i]) - height[i]
        return total

        







            


        