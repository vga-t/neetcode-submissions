# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:
import random
class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 1, n
        while True:
            curr_guess = (low + high)//2
            check = guess(curr_guess)
            if check == -1:

                high = curr_guess - 1
            elif check == 1:
                low = curr_guess + 1
            else:
                return curr_guess 

            
        
        