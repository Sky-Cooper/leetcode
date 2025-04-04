class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i = m - 1
        j = n - 1
        k = m + n - 1

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i = i - 1
            elif j >= 0 and nums1[i] < nums2[j]:
                nums1[k] = nums2[j]
                j = j - 1
            k = k - 1

        return nums1
