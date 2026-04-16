class Solution:
    @staticmethod
    def isPalindrome(s: str) -> bool:
        s_cleaned = ""
        for c in s:
            if c.isalnum():
                s_cleaned += c.lower()
        return s_cleaned == s_cleaned[::-1]
        
    def validPalindrome(self, s: str) -> bool:
        if self.isPalindrome(s):
            return True
        for i in range(len(s)):
            new_s = s[:i] + s[i+1:]  
            if self.isPalindrome(new_s):
                return True
        return False