class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and c != stack[-1] and c.lower() == stack[-1].lower():
                stack.pop()
            else:
                stack.append(c)
        ans = ""
        for c in stack:
            ans += c
        return ans
        
