from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        pair = {')': '(', ']': '[', '}': '{'}
        for char in s:
            if char in "([{":
                l.append(char)
            else:
                if not l or l[-1] != pair[char]:
                    return False
                l.pop()
        return not l
