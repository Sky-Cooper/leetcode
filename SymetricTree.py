class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True

        def is_symetric(val1, val2):
            if not val1 and not val2:
                return True

            if not val1 or not val2:
                return False

            return (
                (val1.val == val2.val)
                and is_symetric(val1.right, val2.left)
                and is_symetric(val1.left, val2.right)
            )

        return is_symetric(root.left, root.right)
