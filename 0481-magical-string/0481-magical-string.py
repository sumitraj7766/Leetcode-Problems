class Solution(object):
    def magicalString(self, n):
        if n == 1:
            return 1 

        s = [1 , 2 , 2]

        i = 2
        num = 1

        while len(s) < n:
            count = s[i]

            for _ in range(count):
                if len(s) == n:
                    break

                s.append(num)

            num = 3 - num
            i += 1

        return s[:n].count(1)




        """
        :type n: int
        :rtype: int
        """
    