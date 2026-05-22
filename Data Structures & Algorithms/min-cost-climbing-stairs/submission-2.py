class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min_costs = cost[:2]
        for elem in cost[2:]:
            min_cost = min(min_costs[-1], min_costs[-2])
            min_costs.append(min_cost + elem)
        
        return min(min_costs[-1], min_costs[-2])