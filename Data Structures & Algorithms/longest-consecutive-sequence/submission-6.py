class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(set(nums))
        current = 1
        longest = 1

        for i in range(1, len(nums)):
            if (nums[i-1] + 1) == nums[i]:
                current += 1
                longest = max(current, longest)
            else:
                current = 1
        return longest

