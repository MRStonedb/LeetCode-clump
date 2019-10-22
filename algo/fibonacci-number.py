"""
给定 N，计算 F(N)。
"""

class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        a, b = 0, 1
        while N:
            a, b = b, a+b
            N -= 1
        return a
    
a =Solution()
print(a.fib(10))
