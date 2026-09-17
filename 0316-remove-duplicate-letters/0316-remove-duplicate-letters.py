class Solution(object):
    def removeDuplicateLetters(self, s):

        last = {}

        for i in range (len(s)):
            last[s[i]] = i

        stack = []

        visited = set()

        for i, c in enumerate(s):
            if c in visited:
                continue

            while (
                stack
                and stack[-1] > c
                and last[stack[-1]] > i):

                removed = stack.pop()
                visited.remove(removed)

            stack.append(c)
            visited.add(c)

        return ''.join(stack)


        
        