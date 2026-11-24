import re
from collections import Counter
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """

        paragraph = paragraph.lower()
        words = re.findall(r'[a-z]+', paragraph)
        banned_set = set(banned)

        freq = Counter()

        for word in words:
            if word not in banned_set:
                freq[word] += 1

        return freq.most_common(1)[0][0]
        