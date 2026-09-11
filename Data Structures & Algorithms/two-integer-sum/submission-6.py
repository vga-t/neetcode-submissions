class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked = {}
        for i, num in enumerate(nums):
            search = target - num
            if search in checked:
                return [checked[search], i]
            checked[num] = i 
