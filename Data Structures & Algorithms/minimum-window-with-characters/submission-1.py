class Solution:
    def is_valid(self, t_count, s_count):
            for char in t_count:
                if s_count.get(char, 0) < t_count[char]:
                    return False
            return True
    def minWindow(self, s: str, t: str) -> str:


        t_count = {}
        for char in t:
            t_count[char] = t_count.get(char, 0) + 1

        L = 0
        res_l, res_r = 0, float('inf')
        s_count = {}

        for R in range(len(s)):
            s_count[s[R]] = s_count.get(s[R], 0) + 1

            while self.is_valid(t_count, s_count):
                if (R - L + 1) < (res_r - res_l +1):
                    res_l = L
                    res_r = R
                s_count[s[L]] -= 1 
                L += 1
        return s[res_l: res_r + 1] if res_r != float("inf") else ""

        

        