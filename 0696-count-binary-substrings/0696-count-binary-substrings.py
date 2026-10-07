class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        prev = 0
        curr = 0
        ans = 0


        for i in range(len(s)):
            if i > 0 and s[i] == s[i-1]:
                curr += 1


            else:

                ans += min(prev , curr)
                prev = curr
                curr = 1

                

        ans += min(prev , curr)

        return ans