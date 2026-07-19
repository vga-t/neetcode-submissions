class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = dict()
        for num in nums:
            frequency[num] = 1 + frequency.get(num,0)
        
        return [x[0] for x in sorted(frequency.items(), key = lambda x:x[1], reverse = True)[:k]]

        
        