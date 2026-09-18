class Solution(object):
    def thirdMax(self, nums):
        first = None
        second = None
        third = None

        for num in nums:

            # Ignore duplicates
            if num == first or num == second or num == third:
                continue

            # New maximum
            if first is None or num > first:
                third = second
                second = first
                first = num

            # New second maximum
            elif second is None or num > second:
                third = second
                second = num

            # New third maximum
            elif third is None or num > third:
                third = num

        # If third maximum doesn't exist
        if third is None:
            return first

        return third