class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        while left < right:
            is_left_character_alpha = self.isAlphaNum(s[left])
            is_right_character_alpha = self.isAlphaNum(s[right])
            if not is_left_character_alpha:
                left+=1
            if not is_right_character_alpha:
                right-=1


            if is_left_character_alpha and is_right_character_alpha:
                if s[left].lower() != s[right].lower():
                    return False
                else:
                    left+=1
                    right-=1

        return True

    def isAlphaNum(self, c):
        if '0'<=c<='9' or 'a'<=c<='z' or 'A'<=c<='Z':
            return True
        else:
            return False
            

            
        