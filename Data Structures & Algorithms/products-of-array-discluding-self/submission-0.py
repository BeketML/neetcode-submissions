class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        new_arr = [1] * len(nums)

        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                product *= nums[j]
            new_arr[i] = product
        return new_arr