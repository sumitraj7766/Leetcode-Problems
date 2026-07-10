class Solution(object):
    def combinationSum3(self, k, n):
        result = []

        def backtrack(start, current, total):
            if len(current) == k:
                if total == n:
                    result.append(current[:])
                return

            for num in range(start, 10):
                if total + num > n:
                    break

                current.append(num)

                backtrack(num + 1, current, total + num)

                current.pop()

        backtrack(1, [], 0)

        return result