class Solution(object):
    def findLongestWord(self, s, dictionary):
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: str
        """

        def isSubsequence(word,s):
            i = 0


            for ch in s:
                if i < len(word) and word[i] == ch:
                    i += 1


            return i == len(word)


        ans = ""

        for word in dictionary:
            if isSubsequence(word , s):
                if len(word) > len(ans):
                    ans = word

                elif len(word) == len(ans) and word < ans:
                    ans = word

        return ans
        