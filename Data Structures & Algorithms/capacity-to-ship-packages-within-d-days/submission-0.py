class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        res = r

        while l <= r:
            mid_weight = (l + r) // 2

            current_days = 1
            current_load = 0

            for weight in weights:
                if weight + current_load > mid_weight:
                    current_days += 1
                    current_load = 0
                current_load += weight
            
            if current_days <= days:
                res = mid_weight
                r = mid_weight - 1
            else:
                l = mid_weight + 1
        return res 



        