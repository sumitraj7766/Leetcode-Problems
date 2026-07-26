class Solution:
    def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        m = len(primes)

        dp = [0] * n
        dp[0] = 1

        ptr = [0] * m

        for i in range(1, n):

            candidates = [primes[j] * dp[ptr[j]] for j in range(m)]

            mn = min(candidates)

            dp[i] = mn

            for j in range(m):
                if candidates[j] == mn:
                    ptr[j] += 1

        return dp[-1]