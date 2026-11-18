
class Solution(object):
    def myPow(self, x, n):
        negative = n < 0
        n = abs(n)

        ans = 1.0

        while n > 0:
            if n % 2 == 1:
                ans *= x

            x *= x
            n //= 2

        if negative:
            ans = 1.0 / ans

        return ans
