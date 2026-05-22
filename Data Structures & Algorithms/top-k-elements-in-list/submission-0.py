class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        res = [0] * k
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        return [num for num, count in sorted(counts.items(), key=lambda item: -item[1])[:k]]

