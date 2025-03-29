class Solution(object):
    def twoSum(self, nums, target):

        indexes = {}

        for i, num in enumerate(nums):

            comp = target - num

            if comp in indexes:
                return [indexes[comp], i]

            indexes[num] = i

        return None


nums = [2, 7, 11, 15]
target = 9

Sol = Solution()
result = Sol.twoSum(nums, target)
print(result)


