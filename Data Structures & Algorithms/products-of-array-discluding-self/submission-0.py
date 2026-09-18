class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        postfix = 1
        length = len(nums)
        postfix_array = [0]*length
        res = []
        for i in range(length-1, -1, -1):
            postfix_array[i] = postfix
            postfix = postfix*nums[i]
        prefix = 1
        for i in range(length):
            res.append(prefix * postfix_array[i])
            prefix = prefix * nums[i]

        return res