class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        words.sort()
        word_set = set(words)
        ans = ""
        

        for word in words:
            valid = True


            for i in range(1, len(word) + 1):
                prefix = word[:i]

                if prefix not in word_set:
                    valid = False

                    break


            if valid and len(word) > len(ans):
                ans = word

        return ans


        