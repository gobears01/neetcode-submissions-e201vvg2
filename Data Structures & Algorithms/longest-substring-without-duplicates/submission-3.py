class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        maxWindow = 0
        seen = set()
        for i in range(len(s)):
            right = i
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            window = right - left + 1
            maxWindow = max(maxWindow, window)
        return maxWindow



        
