class Solution:
    def cleaned(self, text: str) -> str:
        res = ""
        for char in text:
            if char.isalnum():
                res += char.lower()
        return res

    def isPalindrome(self, s: str) -> bool:
        cleaned_text = self.cleaned(s)
        L, R = 0, len(cleaned_text) - 1
        while L < R:
            if cleaned_text[L] != cleaned_text[R]:
                return False
            L += 1
            R -= 1
        return True
        