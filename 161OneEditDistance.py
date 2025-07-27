class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        lens, lent = len(s), len(t)

        if abs(lens-lent) > 1:
            return False

        if lens == lent:
            counter = 0
            for i in range(lens):
                if s[i] != t[i]:
                    counter += 1
                    if counter > 1:
                        return False
            return counter == 1 # True s = "" t = ""   

        elif lens +1 == lent:
            for i in range(lens):
                if s[i] != t[i]:
                    return s[i:] == t[i+1:]
            return True

        elif lent +1 == lens:
            for i in range(lent):
                if s[i] != t[i]:
                    return s[i+1:] == t[i:]
            return True

        return False


        
