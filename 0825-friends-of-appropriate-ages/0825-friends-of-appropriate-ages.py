class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        count = [0]*121

        for age in ages:
            count[age] += 1

        ans = 0
        for x in range(1 , 121):
            for y in range(1 , 121):
                if y > 0.5*x + 7 and y <= x:
                    ans += count[x] * count[y]

                    if x == y:
                        ans -= count[x]


            

        return ans