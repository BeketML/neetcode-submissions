from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        bucket = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            bucket[key].append(s)
        return list(bucket.values())
        