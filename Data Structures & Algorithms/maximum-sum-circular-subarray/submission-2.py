class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # i need:
        # total_sum
        # max_subarray 
        # min_subarray 

        total_sum = 0

        curr_max = 0
        max_subarray = nums[0]

        curr_min = 0
        min_subarray = nums[0]

        for i in range(len(nums)):

            # kadane for max subarray
            curr_max = max(curr_max+nums[i], nums[i])
            max_subarray = max(curr_max, max_subarray)

            # kadane for min subarray
            curr_min = min(curr_min + nums[i], nums[i])
            min_subarray = min(curr_min, min_subarray)

            total_sum += nums[i]
        if max_subarray < 0:
            return max_subarray
        return max(total_sum - min_subarray, max_subarray)


  
        