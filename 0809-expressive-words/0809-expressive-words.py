
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

               
                if s[i] != word[j]:
                    return False

                
                start_i = i

                while i < len(s) and s[i] == s[start_i]:
                    i += 1

                
                start_j = j

                while j < len(word) and word[j] == word[start_j]:
                    j += 1

                s_count = i - start_i
                word_count = j - start_j

                
                if s_count == word_count:
                    continue

                if s_count >= 3 and s_count > word_count:
                    continue

                return False

            
            return i == len(s) and j == len(word)

        answer = 0

        for word in words:
            if is_stretchy(word):
                answer += 1

        return answer

