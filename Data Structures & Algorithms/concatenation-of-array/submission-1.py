class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new_arr = []
        for i in range(2):
            for n in nums:
                new_arr.append(n)
        return new_arr