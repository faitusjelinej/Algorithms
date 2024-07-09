class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []

        s = nums[0]
        res = []

        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]+1:
                continue
            else:
                if s == nums[i-1]:
                    res.append(str(s))
                else:
                    res.append(str(s)+"->"+str(nums[i-1]))    

                s = nums[i]

        if s != nums[-1]:
            res.append(str(s)+"->"+str(nums[-1]))
        else:
            res.append(str(s))

        return res                           
