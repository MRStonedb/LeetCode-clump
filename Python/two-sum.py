#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# 返回列表中 两个数之和等于某个给定数的下标
class Solution:
    # 两次循环
    def twoSum(self, nums, target):
        size = len(nums)
        for i,num in enumerate(nums):
            j = i+1
            while j<size:
                if target == num + nums[j]:
                    return [i,j]
                else:
                    j += 1

    # 字典模拟哈希（两次）
    def tow_sum_with_dict(self, nums, target):
        _dict = {}
        for i, m in enumerate(nums):
            _dict[m] = i

        for i, m in enumerate(nums):
            j = _dict.get(target - m)
            if j is not None and i != j:
                return [i, j]

    # 字典模拟哈希（一次）
    def tow_sum_with_dict2(self, nums, target):
        _dict = {}
        for i, m in enumerate(nums):
            if _dict.get(target - m) is not None:
                return [_dict.get(target - m), i]
            _dict[m] = i

 
nums = [2,5,5,7,8,5]
target = 10
s = Solution()
print(s.twoSum(nums, target))
print(s.tow_sum_with_dict(nums, target))
print(s.tow_sum_with_dict2(nums, target))   