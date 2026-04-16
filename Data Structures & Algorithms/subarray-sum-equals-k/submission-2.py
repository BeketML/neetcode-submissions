from collections import defaultdict

class Solution:
    def subarraySum(self, nums, k):
        prefix = defaultdict(int)
        prefix[0] = 1
        
        curr_sum = 0
        cnt = 0
        
        for num in nums:
            curr_sum += num
            
            if curr_sum - k in prefix:
                cnt += prefix[curr_sum - k]
            
            prefix[curr_sum] += 1
        
        return cnt
