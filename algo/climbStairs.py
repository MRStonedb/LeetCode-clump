"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
注意：给定 n 是一个正整数。
"""


class soloution():
    def climbStairs(self, n):
        p = 1
        q = 2
        if n == 1:
            return 1
        if n == 2:
            return 2
        for _ in range(2,n):
            p,q = q, p+q

        return q


n = 10
s = soloution()
print(s.climbStairs(n))
