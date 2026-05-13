class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_sum = 0
        max_l, max_r = 0, 0
        L = 0

        for R in range(len(nums)):
            if curr_sum < 0:
                curr_sum = 0
                L = R
            
            curr_sum += nums[R]
            if curr_sum > max_sum:
                max_sum = curr_sum
                max_l, max_r = R, L
        return max_sum

                