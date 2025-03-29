class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        symbol_value = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        subtracted_combinaison = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
        }

        total = 0
        i = 0

        while i < len(s):

            if i + 1 < len(s) and s[i : i + 2] in subtracted_combinaison:
                total = total + subtracted_combinaison[s[i : i + 2]]
                i = i + 2

            else:
                total = total + symbol_value[s[i]]
                i = i + 1

        return total
