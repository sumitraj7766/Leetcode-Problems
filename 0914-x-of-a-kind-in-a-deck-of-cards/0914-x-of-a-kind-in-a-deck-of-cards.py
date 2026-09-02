class Solution(object):
    def hasGroupsSizeX(self, deck):
        def gcd(a,b):
            while b:
                a, b = b, a%b
            return a
        

        freq = {}

        for card in deck:
            freq[card] = freq.get(card, 0) + 1

        g = 0

        for count in freq.values():
            g = gcd(g, count)

        return g >= 2