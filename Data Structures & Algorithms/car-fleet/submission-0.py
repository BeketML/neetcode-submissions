class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_pos = sorted(zip(position, speed), reverse = True)

        curr_time = 0
        fleet = 0

        for pos, sp in sorted_pos:
            time = (target - pos) / sp

            if time > curr_time:
                curr_time = time
                fleet += 1
        return fleet

        