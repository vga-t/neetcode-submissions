class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        unique_triplets = []
        nums.sort()
        length = len(nums)
        for first in range(length-2):
            second, third = first + 1, length - 1
            if first > 0 and nums[first] == nums[first-1]:
                continue
            while second < third:
                
                if (second > first + 1) and nums[second] == nums[second - 1 ]:
                    second += 1
                    continue
                if (third < length -1) and nums[third] == nums[third + 1]:
                    third -= 1
                    continue
                
                if nums[first] + nums[second] + nums[third] == 0:
                    unique_triplets.append([nums[first], nums[second], nums[third]])
                    second +=1
                elif nums[first] + nums[second] + nums[third] > 0:
                    third -= 1
                else:
                    second += 1
        return unique_triplets

        