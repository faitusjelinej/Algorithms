class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        res = []

        if len(nums) == 0:
            return [[lower, upper]]

        if nums[0] > lower:
            res.append([lower, nums[0]-1])

        for i in range(1,len(nums)):
            if nums[i-1]+1 != nums[i]:
                res.append([nums[i-1]+1, nums[i]-1])

        if nums[-1]< upper:
            res.append([nums[-1]+1, upper])

        return res                    
