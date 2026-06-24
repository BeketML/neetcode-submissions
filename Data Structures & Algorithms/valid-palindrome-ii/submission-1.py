class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1
            return True

        L, R = 0, len(s) - 1
        while L < R:
            if s[L] != s[R]:
                return check(L + 1, R) or check(L, R - 1)

            L += 1
            R -= 1
        return True
        
        
        
        