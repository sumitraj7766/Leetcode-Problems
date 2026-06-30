class Solution(object):
    def wordBreak(self, s, wordDict):
        wordset = set(wordDict)

        max_len = max(len(word) for word in wordDict)

        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for length in range(1, max_len + 1):

                if i - length < 0:
                    break

                if dp[i - length] and s[i - length:i] in wordset:
                    dp[i] = True
                    break

        return dp[len(s)]