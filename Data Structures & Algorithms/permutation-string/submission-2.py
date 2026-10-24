from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        target = Counter(s1)
        n = len(s2)

        for left in range(n):

            count = target.copy()
            needed = len(s1)

            right = left

            while right < n and s2[right] in count:

                if count[s2[right]] == 0:
                    break

                count[s2[right]] -= 1
                needed -= 1

                if needed == 0:
                    return True

                right += 1

        return False



        