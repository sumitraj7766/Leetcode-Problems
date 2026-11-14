class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort(key=lambda x: x[1])
        arrows = 1
        arrow = points[0][1]

        for start,end in points:
            if start > arrow:
                arrows += 1
                arrow = end


        return arrows