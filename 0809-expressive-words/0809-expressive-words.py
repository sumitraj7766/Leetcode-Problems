
class Solution(object):
    def expressiveWords(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """

        def is_stretchy(word):

            i = 0
            j = 0

            while i < len(s) and j < len(word):

                # Characters must be the same
                if s[i] != word[j]:
                    return False

                # Count same characters in s
                start_i = i

                while i < len(s) and s[i] == s[start_i]:
                    i += 1

                # Count same characters in word
                start_j = j

                while j < len(word) and word[j] == word[start_j]:
                    j += 1

                s_count = i - start_i
                word_count = j - start_j

                # Check whether this group can be stretched
                if s_count == word_count:
                    continue

                if s_count >= 3 and s_count > word_count:
                    continue

                return False

            # Both strings must be completely processed
            return i == len(s) and j == len(word)

        answer = 0

        for word in words:
            if is_stretchy(word):
                answer += 1

        return answer

