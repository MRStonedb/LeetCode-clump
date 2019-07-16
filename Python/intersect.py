#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# 两个列表的交集

class solution():
    def intersect(self,nums1,nums2):
        nums1.sort()
        nums2.sort()
        r = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                r.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

        return r


nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
s =solution()
print(s.intersect(nums1,nums2))