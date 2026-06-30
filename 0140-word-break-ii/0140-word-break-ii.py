class Solution(object):
    def wordBreak(self, s, wordDict):
        wordset = set(wordDict)
        memo = {}

        def backtrack(start):
            if start == len(s):
                return [""]

            if start in memo:
                return memo[start]

            sentences = []

            for end in range(start + 1, len(s) + 1):
                word = s[start:end]

                if word in wordset:
                    rest_sentences = backtrack(end)
                    for sentence in rest_sentences:
                        if sentence == "":
                            sentences.append(word)

                        else:
                            sentences.append(word + " " + sentence)
            memo[start] = sentences
            return sentences

        return backtrack(0)

