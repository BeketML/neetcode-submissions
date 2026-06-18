class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        L = 0

        for R in range(len(arr)):
            if  (R - L + 1) > k:
                distance_l = abs(arr[L] - x)
                distance_r = abs(arr[R] - x)

                if distance_r < distance_l:
                    L += 1
                else:
                    pass
        return arr[L: L + k]

        