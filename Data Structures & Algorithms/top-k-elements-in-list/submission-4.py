class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [set() for _ in range(len(nums))]
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            if counts[num] > 1:
                buckets[counts[num] - 2].remove(num)
            buckets[counts[num] - 1].add(num)
        
        top_k = []
        for l in buckets[::-1]:
            for elem in l:
                top_k.append(elem)
                if len(top_k) == k:
                    return top_k

