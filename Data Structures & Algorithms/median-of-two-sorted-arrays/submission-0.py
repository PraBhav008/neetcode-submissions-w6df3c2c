class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = j = 0
        res = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1

        # add remaining elements
        while i < len(nums1):
            res.append(nums1[i])
            i += 1

        while j < len(nums2):
            res.append(nums2[j])
            j += 1

        length = len(res)
        l, h = 0, length - 1
        if length % 2 == 0:
            m1 = length // 2 - 1
            m2 = length // 2

            med = (res[m1] + res[m2]) / 2
            return med
        else:
            m = (l + h) // 2
            return res[m]