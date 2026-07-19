class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            # Local bindings (faster than repeated attribute lookups)
            c_left = s[left]
            c_right = s[right]

            # ASCII-only alphanumeric check (much faster than isalnum)
            is_left_alpha = (
                ('0' <= c_left <= '9') or
                ('a' <= c_left <= 'z') or
                ('A' <= c_left <= 'Z')
            )
            is_right_alpha = (
                ('0' <= c_right <= '9') or
                ('a' <= c_right <= 'z') or
                ('A' <= c_right <= 'Z')
            )

            if not is_left_alpha:
                left += 1
                continue

            if not is_right_alpha:
                right -= 1
                continue

            # ASCII lowercase conversion (faster than .lower())
            if 'A' <= c_left <= 'Z':
                c_left = chr(ord(c_left) + 32)
            if 'A' <= c_right <= 'Z':
                c_right = chr(ord(c_right) + 32)

            if c_left != c_right:
                return False

            left += 1
            right -= 1

        return True
