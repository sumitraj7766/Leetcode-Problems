class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """

        answer = []
        positions = []

        for i in range(len(s)):
            if s[i] == c:
                positions.append(i)


        for i in range(len(s)):
            distances = []
            for pos in positions:
                distances.append(abs(i - pos))
            answer.append(min(distances))

        return answer
        