#!/usr/bin/env python
# -*- encoding: utf-8 -*-


# 爬楼梯


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