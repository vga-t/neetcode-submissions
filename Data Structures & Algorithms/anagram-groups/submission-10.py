from collections import Counter, defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        list_of_anagram = defaultdict(list)
        for string in strs:
            key = tuple(sorted(Counter(string).items()))
            list_of_anagram[tuple(key)].append(string)

        return list(list_of_anagram.values())