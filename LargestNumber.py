# 179. Largest Number - leetcode


#Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.
#Since the result may be very large, so you need to return a string instead of an integer.

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if str(nums[i]) + str(nums[j])  > str(nums[j]) + str(nums[i]):
                    continue
                else:
                    nums[i], nums[j] =   nums[j], nums[i]  #swap
        res = "".join(str(i) for i in nums)
        return str(int(res))             
