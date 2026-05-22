import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        high = max(piles)
        low = 1
        best_k = (high, h - len(piles))

        while low <= high:
            k = (high + low) // 2
            total_time = self.bananaTime(piles, k)
            
            # not enough time, increase eating rate
            if total_time > h:
                low = k + 1
            # we have extra time, lower eating rate
            else:
                high = k - 1
                distance = h - total_time
                if distance <= best_k[1] and k < best_k[0]:
                    best_k = (k, distance)

        return best_k[0]

    def bananaTime(self, piles, k):
        total_time = 0
        for pile in piles:
            total_time += math.ceil(pile/k)
        return total_time
