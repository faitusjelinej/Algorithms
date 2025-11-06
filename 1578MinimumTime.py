class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total = 0
        for i in range(1,len(neededTime)):
            if colors[i] == colors[i-1]:
                total += min(neededTime[i], neededTime[i-1])
                neededTime[i] = max(neededTime[i],neededTime[i-1])
        return total        
