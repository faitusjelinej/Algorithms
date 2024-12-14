class Solution:
    def countSubstrings(self, s: str) -> int:
        def paliandormcheck(s,l,r):
            res = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            return res    

        output = 0
        for i in range(len(s)):
            output +=   paliandormcheck(s,i,i) 
            output +=   paliandormcheck(s,i,i+1)   
        return output    
