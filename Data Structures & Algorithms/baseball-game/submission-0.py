from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        records = []
        
        for record in operations:
            if record == "+":
                # Сумма двух последних
                records.append(records[-1] + records[-2])
            elif record == "D":
                # Удвоение последнего
                records.append(2 * records[-1])
            elif record == "C":
                # Удаление последнего (Pop)
                records.pop()
            else:
                # Если это число (включая отрицательные и многозначные)
                records.append(int(record))
                
        return sum(records)