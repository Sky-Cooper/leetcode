class Solution(object):
    def isValid(self, s):
        brakets_dict = {
            "}": "{",
            "]": "[",
            ")": "(",
        }

        stack = []

        for char in s:
            if char in brakets_dict.values():
                stack.append(char)

            elif char in brakets_dict:
                if not stack or stack[-1] != brakets_dict[char]:
                    return False
                stack.pop()

        return True if not stack else False
