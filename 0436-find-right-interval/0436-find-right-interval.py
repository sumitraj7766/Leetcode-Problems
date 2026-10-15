import bisect
class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """

        n = len(intervals)
        pairs = sorted((start, i) for i, (start, end) in enumerate(intervals))

        start_vals = [s for s, _ in pairs]

        result = [-1] * n
        for i, (start, end) in enumerate(intervals):
            pos = bisect.bisect_left(start_vals, end)
            if pos < n:
                result[i] = pairs[pos][1]

        return result

        