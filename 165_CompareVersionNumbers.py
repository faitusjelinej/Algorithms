class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        level1 = version1.split(".")
        level2 = version2.split(".")

        maxlen = max(len(level1), len(level2))

        for i in range(maxlen):
            if i < len(level1):
                v1 = int(level1[i])
            else:
                v1 = 0
            if i < len(level2):
                v2 = int(level2[i])
            else:
                v2 = 0

            if v1 < v2:
                return -1
            elif v1 > v2:
                return 1

        return 0 
