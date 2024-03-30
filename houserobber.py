class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        option1 = nums[0]
        option2 = nums[1]

        for i in range(2, len(nums)):
            if (i%2 == 0):
                option2 = max(option1, option2)
                option1 += nums[i]
            else:
                option1 = max(option1, option2)
                option2 += nums[i] 
        return max(option1, option2)                   
