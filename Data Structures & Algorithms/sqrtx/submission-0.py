class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        l = 0
        r = x // 2
        ans = 0

        while l <= r:
            mid = (l + r) // 2
            num = mid * mid

            if num == x:
                return mid
            elif num < x:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans

        