class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        maping = { ")" : "(", "]" : "[", "}" : "{" }
        for char in s:
            if char in maping:
                if stack and stack[-1] == maping[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False

    

