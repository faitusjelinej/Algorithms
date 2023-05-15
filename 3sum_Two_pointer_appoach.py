# First sort the array. use a for loop to iterate one index and then use two pointers approach

def threeSum(nums):
    nums.sort()
    res = []

    for i in range(len(nums)):
        if i > 0 and nums[i]== nums[i-1]:
            continue

        l = i+1
        r = len(nums)-1

        while l < r:
            total =  nums[i] + nums[l] + nums[r]
            if total == 0:
                res.append([nums[i],nums[l],nums[r]])
                while r < l and nums[l] == nums[l+1]:
                    l += 1
                while r < l and  nums[r] == nums[r-1]:
                    r -= 1
                l += 1
                r -= 1
            elif total > 0:
                r -= 1
            else:
                l += 1
    return res

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))
