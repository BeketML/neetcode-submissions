class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_cleaned = ""
        for c in s:
            if c.isalnum():
                s_cleaned+=c.lower()
        return s_cleaned == s_cleaned[::-1]

        