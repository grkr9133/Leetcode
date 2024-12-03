#Leetcode Problem 746
#Author: Radhakrishna Rakesh Grandi
# Updated on December 03, 2024

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        for i in range(len(cost)-3,-1,-1): # we are traversing the list from right end and we start at index -3
            cost[i]+=min(cost[i+1],cost[i+2])
        return min(cost[0],cost[1])

