class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        freq = {}
        res = 0
        for i in range(len(s)):
            right = i
            freq[s[right]] = 1 + freq.get(s[right], 0)
            window = right - left + 1
            while (window - max(freq.values())) > k:
                freq[s[left]] -= 1
                left += 1
                window = right - left + 1
            res = max(res, window)
        return res

