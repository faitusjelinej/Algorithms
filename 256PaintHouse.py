class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        dp = [[0 for i in range(3)] for j in range(len(costs))]

        for cost in range(len(costs)):
            for color in range(3):
                if cost == 0:
                    dp[cost][color] = costs[cost][color]
                else:
                    if color == 0:
                        dp[cost][color] = costs[cost][color] + min(dp[cost-1][1],dp[cost-1][2])
                    if color == 1:
                        dp[cost][color] = costs[cost][color] + min(dp[cost-1][0],dp[cost-1][2])
                    if color == 2:
                        dp[cost][color] = costs[cost][color] + min(dp[cost-1][0],dp[cost-1][1])        
        return min(dp[-1])                                
