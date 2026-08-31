class Solution(object):
    def frequencySort(self, s):
        freq = {}

        # Count frequency
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        # Sort characters by frequency
        chars = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        # Build answer
        ans = ""

        for ch, count in chars:
            ans += ch * count

        return ans