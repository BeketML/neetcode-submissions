class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l, res, prev = 0, 1, ""
        for r in range(len(arr)-1):
            if arr[r] > arr[r+1] and prev != ">":
                res = max(res, r - l + 2)
                prev = ">"
            elif arr[r] < arr[r+1] and prev != "<":
                res = max(res, r - l + 2)
                prev = "<"
            else:
                l = r if arr[r] != arr[r+1] else r + 1
                res = max(res, r - l + 2 if arr[r] != arr[r+1] else 1)
                prev = ">" if arr[r] > arr[r+1] else ("<" if arr[r] < arr[r+1] else "")
        return res