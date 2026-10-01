class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        unique_triplets = set()
        nums.sort()
        length = len(nums)
        for first in range(length-2):
            second, third = first + 1, length - 1
            if first > 0 and nums[first] == nums[first-1]:
                continue
            while second < third:
                # print((nums[first], nums[second], nums[third]))
                if nums[first] + nums[second] + nums[third] == 0:
                    unique_triplets.add((nums[first], nums[second], nums[third]))
                    second +=1
                elif nums[first] + nums[second] + nums[third] > 0:
                    third -= 1
                else:
                    second += 1
        return [list(unique) for unique in unique_triplets]

        