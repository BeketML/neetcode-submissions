class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new_arr = [0] * (len(nums) * 2)
        for i in range(len(nums)):
            new_arr[i] = nums[i]
        
        for j in range(len(nums)):
            new_arr[len(nums) + j] = nums[j]
        
        return new_arr