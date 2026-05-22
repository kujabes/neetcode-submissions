class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        total_cost = 0
        curr_idx = len(cost)
        
        # if it is still possible to traverse
        while (curr_idx - 2) >= 0:
            idx1 = curr_idx - 1
            idx2 = curr_idx - 2
            # choose the lower of the two elements
            if cost[idx1] < cost[idx2]:
                curr_idx = idx1
            else:
                curr_idx = idx2
            
            total_cost += cost[curr_idx]
        
        return total_cost

