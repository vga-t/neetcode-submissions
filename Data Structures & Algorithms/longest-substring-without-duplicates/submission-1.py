class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        left, right = 0, 0
        length = 0

        for char in s:
            while char in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(char)
            length = max(length, right - left + 1)
            right += 1
        return length







        
        