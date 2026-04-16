class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = {}
        for num in nums:
            if num in cnt:
                cnt[num] += 1
            else:
                cnt[num] = 1
        
        sorted_keys = sorted(cnt, key = cnt.get, reverse = True)
        return sorted_keys[:k]

        