class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: list[int], target: int) -> int:
        s = 0
        for i in hours:
            if i >= target:
                s += 1
        return s

