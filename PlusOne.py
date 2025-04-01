class Solution(object):
    def plusOne(self, digits):
        if digits[-1] != 9:
            digits[-1] += 1
            return digits

        counter = 0
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] != 9:
                break
            counter += 1

        if len(digits) == counter:
            return [1] + [0] * counter

        digits[len(digits) - 1 - counter] = 1

        for i in range(len(digits) - 1 - counter, len(digits)):
            digits[i] = 0

        return digits
