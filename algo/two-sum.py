"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
"""

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



class SolutionA(object):
    @staticmethod
    def twoSum(nums, target):
        """
        静态方法，省去对象初始化，节省时间
        """
        num_dict = {}
        for index, value in enumerate(nums):
            another_num = target - value
            if another_num in num_dict:
                return [num_dict[another_num], index]
            num_dict[value] = index
        return None
                
nums = [2, 7, 11, 15]
target = 17          
print(SolutionA.twoSum(nums, target))


 
nums = [2,5,5,7,8,5]
target = 10
s = Solution()
print(s.twoSum(nums, target))
print(s.tow_sum_with_dict(nums, target))
print(s.tow_sum_with_dict2(nums, target))   