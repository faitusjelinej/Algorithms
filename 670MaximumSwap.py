class Solution:
    def maximumSwap(self, num: int) -> int:
        maxindex = len(str(num))-1
        xi = yi = 0

        nums = list(str(num))

        for i in range(len(nums)-1,-1,-1):
            if nums[i] > nums[maxindex]:
                maxindex = i
            elif nums[i] < nums[maxindex]:
                xi = i
                yi = maxindex
        nums[xi], nums[yi] = nums[yi], nums[xi]

        return int("".join(str(x) for x in nums))          
