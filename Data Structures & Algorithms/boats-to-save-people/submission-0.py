class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        res = 0
        l = 0
        r = len(people) - 1

        while l <= r:
            res+=1
            summ = people[l] + people[r]
            if summ <= limit:
                l+=1
            r-=1
        return res
        