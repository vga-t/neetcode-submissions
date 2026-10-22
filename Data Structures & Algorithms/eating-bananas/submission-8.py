import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maximum_speed = max(piles)
        def check_hours(speed):
            length = len(piles)
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/speed) 
            return hours

        left, right = 1, maximum_speed
        while left<=right:
            mid = (left+right)//2
            if check_hours(mid) > h:
                left = mid + 1
            else:
                right = mid - 1
        return left

  



        