class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in numSet:
                size = 0
                while num in numSet:
                    size+=1
                    num+=1
                longest = max(longest, size)
        return longest
                    



        