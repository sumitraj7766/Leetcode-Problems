class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """

        houses.sort()
        heaters.sort()

        radius = 0
        j =0

        for house in houses:
            while j < len(heaters) - 1 and \
            abs(heaters[j + 1] - house) <= abs(heaters[j] - house):
                j += 1

            distance = abs(heaters[j] - house)
            radius = max(radius , distance)

        return radius

        