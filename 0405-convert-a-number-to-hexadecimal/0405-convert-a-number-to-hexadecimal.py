class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """

        if num == 0:
            return "0"

        hex_chars = "0123456789abcdef"

        num = num & 0xffffffff

        result = []
        while num > 0:
            digit = num & 15
            result.append(hex_chars[digit])

            num >>= 4


        result.reverse()
        return "".join(result)
        