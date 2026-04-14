class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        left = 0
        right = 0
        seen = set()
        for i in range(len(s)):
            right = i
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            window = right - left + 1
            maxLen = max(maxLen, window)
        return maxLen


        
