class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        unique_triplets = []
        nums.sort()
        length = len(nums)
        for first in range(length-2):
            
            if first > 0 and nums[first] == nums[first-1]:
                continue
            second, third = first + 1, length - 1
            while second < third:  
                total = nums[first] + nums[second] + nums[third]
                if total == 0:
                    unique_triplets.append([nums[first], nums[second], nums[third]])
                    second += 1
                    third -= 1
                    while second < third and nums[second] == nums[second - 1]:
                        second += 1
                    while second < third and nums[third] == nums[third + 1]:
                        third -= 1
                elif total > 0:
                    third -= 1
                else:
                    second += 1
        
        return unique_triplets



        