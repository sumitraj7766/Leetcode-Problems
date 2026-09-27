class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

        if len(p) > len(s):
            return []

        result = []

        p_count = [0] * 26
        window_count = [0] * 26

        for ch in p:
            p_count[ord(ch) - ord('a')] += 1

        for i in range(len(p)):
            window_count[ord(s[i]) - ord('a')] += 1

        if window_count == p_count:
            result.append(0)

        for right in range(len(p) , len(s)):
            left_char = s[right - len(p)]
            window_count[ord(left_char) - ord('a')] -= 1

            right_char = s[right]
            window_count[ord(right_char) - ord('a')] += 1

            if window_count == p_count:
                result.append(right - len(p) + 1)

        return result

        


        