class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums_set = sorted(list(set(nums)))
        max_streak = 1
        current_streak = 1
        for i in range(1, len(nums_set)):
            if nums_set[i] == nums_set[i-1] + 1:
                current_streak+=1
            else:
                max_streak = max(max_streak, current_streak)
                current_streak=1
        return max(max_streak, current_streak)