class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        for i in range(len(temperatures)):
            count = 1
            j = i + 1
            while j < len(temperatures):
                if temperatures[i] < temperatures[j]:
                    break
                j += 1
                count += 1

            count = 0 if j == len(temperatures) else count
            stack.append(count)
        return stack



        