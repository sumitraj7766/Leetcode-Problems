class Solution(object):
    def findMinDifference(self, timepoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        minutes_list = []

        for time in timepoints:
            total = int(time[:2]) * 60 + int(time[3:])

            minutes_list.append(total)

        minutes_list.sort()

        minimum = 1440 - minutes_list[-1] + minutes_list[0]

        for i in range(1, len(minutes_list)):
            diff = minutes_list[i] - minutes_list[i - 1]
            minimum = min(minimum, diff)

            if minimum == 0:
                return 0 

        return minimum