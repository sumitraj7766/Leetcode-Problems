
from collections import Counter
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = Counter(s)
        chars = sorted(freq.keys(), key=lambda ch: freq[ch], reverse=True)

        result = ""
        for ch in chars:
            result += ch * freq[ch]

        return result


        