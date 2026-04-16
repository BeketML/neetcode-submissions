class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lowest = 0
        highest = len(nums) - 1

        while lowest <= highest:
            mid = (lowest + highest) // 2

            if nums[mid] == target:
                return mid
            
            elif nums[mid] < target:
                lowest = mid + 1
            else:
                highest = mid - 1

        return -1


        
        