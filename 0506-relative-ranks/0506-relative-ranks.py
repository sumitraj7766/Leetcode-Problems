class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        n = len(score)
        answer = [""] * n

        sorted_scores = sorted(range(n), key=lambda i: score[i], reverse=True)

        for rank, index in enumerate(sorted_scores, start=1):
            if rank == 1:
                answer[index] = "Gold Medal"

            elif rank == 2:
                answer[index] = "Silver Medal"

            elif rank == 3:
                answer[index] = "Bronze Medal"

            else:
                answer[index] = str(rank)

        return answer