def canJump(nums):
    last_position = len(nums)-1
            
    for i in range(len(nums)-2,-1,-1):
        if (i + nums[i]) >= last_position:
            last_position = i 
    return last_position == 0


nums = [3,2,1,0,4]
print(canJump(nums))
