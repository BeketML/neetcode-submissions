class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        L = 0
        for R in range(len(nums)):
            if (R - L + 1) >= k:
                res.append(max(nums[L: R + 1]))
                L += 1
        return res
        