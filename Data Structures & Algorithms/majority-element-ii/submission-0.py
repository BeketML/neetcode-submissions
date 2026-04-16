class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        threshold = len(nums) // 3
        nums_cnt = {}
        nums_mjr = []
        for i in range(len(nums)):
            if nums[i] not in nums_cnt.keys():
                nums_cnt[nums[i]] = 0
            nums_cnt[nums[i]] += 1
        
        for key, value in nums_cnt.items():
            if value > threshold:
                nums_mjr.append(key)
        
        return nums_mjr
        

        