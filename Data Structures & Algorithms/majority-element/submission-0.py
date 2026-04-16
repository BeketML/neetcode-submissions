class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnts = {}
        for num in nums:
            if num not in cnts:
                cnts[num] = 1
            else:
                cnts[num]+=1
        return max(cnts, key = cnts.get)
        