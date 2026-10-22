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
            # if speeds[mid] == check_hours(speeds[mid]):
            #     return check_hours()
            if h >= check_hours(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left







        # length = len(piles)
        # for consume in range(1,max(piles)+1):
        #     hours = 0
        #     for pile in piles:
        #         hours += math.ceil(pile/consume) 
        #         if hours > h:
        #             break
            
        #     if hours <= h:
        #         return consume
                



        