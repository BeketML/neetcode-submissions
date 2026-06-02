class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        target_sum = threshold * k
        window_sum = 0
        answer = 0

        for R in range(len(arr)):
            window_sum += arr[R]
            if R >= k - 1:
                if window_sum >= target_sum:
                    answer += 1
                window_sum -= arr[R - k + 1]
        return answer
                
            
                

        