class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        check_dict = {')':'(','}':'{',']':'['}
        for bracket in s:
            if bracket in check_dict.values():
                stack.append(bracket)
            else:
                if (not stack) or check_dict[bracket] != stack.pop():
                    return False
        return not stack