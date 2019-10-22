"""
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
请你找出这两个有序数组的中位数
"""

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        li = sorted((nums1 + nums2))
        s = len(li)
        if s % 2:
            return float(li[s // 2])
        else:
            return float((li[s // 2 - 1] + li[s // 2]) / 2)   
l1 = [1, 2] 
l2 = [3, 4]
s = Solution()
print(s.findMedianSortedArrays(l1, l2))
