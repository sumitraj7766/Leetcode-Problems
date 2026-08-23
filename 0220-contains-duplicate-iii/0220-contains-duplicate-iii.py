class Solution:
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        width = valueDiff + 1
        buckets = {}

        for i, x in enumerate(nums):

            # Remove element outside the sliding window
            if i > indexDiff:
                old = nums[i - indexDiff - 1]
                old_bucket = old // width
                del buckets[old_bucket]

            bucket = x // width

            # Same bucket
            if bucket in buckets:
                return True

            # Left neighboring bucket
            if bucket - 1 in buckets:
                if abs(x - buckets[bucket - 1]) <= valueDiff:
                    return True

            # Right neighboring bucket
            if bucket + 1 in buckets:
                if abs(x - buckets[bucket + 1]) <= valueDiff:
                    return True

            # Insert current value
            buckets[bucket] = x

        return False