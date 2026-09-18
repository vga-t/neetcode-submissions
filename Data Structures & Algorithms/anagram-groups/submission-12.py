from collections import Counter, defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        list_of_anagram = defaultdict(list)
        for s in strs:
            key = [0]*26
            for c in s:
                key[ord(c)-ord('a')]+=1
            list_of_anagram[tuple(key)].append(s)
        return list(list_of_anagram.values())
