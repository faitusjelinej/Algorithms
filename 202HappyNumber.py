class Solution:
    def isHappy(self, n: int) -> bool:
        nset = set()

        while n != 1:
            n = sum([int(i)**2 for i in str(n)])

            if n in nset:
                return False
            else:
                nset.add(n)    

        return True        
