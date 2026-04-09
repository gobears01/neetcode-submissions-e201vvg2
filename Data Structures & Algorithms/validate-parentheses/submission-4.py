class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matchPair = {")": "(","}": "{","]": "[" }
        for i in range(len(s)):
            if s[i] in matchPair:
                if stack == []:
                    return False
                lastParen = stack.pop()
                if matchPair[s[i]] != lastParen:
                    return False
                continue
            stack.append(s[i])
        return stack == []