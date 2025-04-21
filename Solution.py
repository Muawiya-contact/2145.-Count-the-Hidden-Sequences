class Solution(object):
    def numberOfArrays(self, differences, lower, upper):
        curr = 0
        min_sum = 0
        max_sum = 0

        for diff in differences:
            curr += diff
            min_sum = min(min_sum, curr)
            max_sum = max(max_sum, curr)

        low_x = lower - min_sum
        high_x = upper - max_sum

        return max(0, high_x - low_x + 1)
