class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        list1 = []
        list2 = []

        for i in s:
            list1.append(s.index(i))

        for i in t:
            list2.append(t.index(i))

        if list1 == list2:
            return True
        else:
            return False            

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))
