class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        output = []

        intervals = sorted(intervals, key = lambda x: x[0])

        for interval in intervals:
            if not output or output[-1][1] < interval[0]:
                output.append(interval)

            else:
                output[-1][1] = max(output[-1][1], interval[1])

        return output            
