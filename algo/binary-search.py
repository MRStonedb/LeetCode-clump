"""
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，
如果目标值存在返回下标，否则返回 -1。

"""
class Solution(object):
    def search(self, nums, target):
        """ 非递归实现 """
        first = 0
        last = len(nums) - 1
        while first <= last:
            mid = (last+first)//2
            if nums[mid] > target:
                last = mid - 1
            elif nums[mid] < target:
                first = mid + 1
            else:
                return mid-1
        return -1
    def search1(self, nums, target):
        """ 递归实现 """
        n = len(nums)
        if n < 1:
            return -1
        mid = n // 2
        if nums[mid] > target:
            return self.search1(nums[0:mid], target)
        elif nums[mid] < target:
            return self.search1(nums[mid+1:], target)
        else:
            return -1
