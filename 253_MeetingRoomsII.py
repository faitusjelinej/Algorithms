class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = [i[0] for i in intervals]
        end = [i[1] for i in intervals]

        start.sort()
        end.sort()

        s = 0
        e = 0
        count = 0
        output = 0

        while s < len(start):
            if start[s] < end[e]:
                count += 1
                s += 1
            else:
                e += 1
                count -= 1
            output = max(output,count)
        return output            
