
class Solution(object):
    def restoreIpAddresses(self, s):
        result = []

        def backtrack(start, parts):
            if len(parts) == 4:
                if start == len(s):
                    result.append(".".join(parts))
                return

            for length in range(1, 4):
                if start + length > len(s):
                    break

                part = s[start:start + length]

                # Reject leading zeros
                if len(part) > 1 and part[0] == '0':
                    continue

                # Reject values greater than 255
                if int(part) > 255:
                    continue

                parts.append(part)
                backtrack(start + length, parts)
                parts.pop()

        backtrack(0, [])
        return result