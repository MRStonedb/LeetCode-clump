#!/usr/bin/env python
# -*- encoding: utf-8 -*-

#字符串中的第一个唯一字符

import collections

class solution():
    def firstuniqchar(self, s):
        s_counts = collections.Counter(s)
        print(s_counts)
        for i in range(len(s)):
            if s_counts[s[i]] <= 1:
                return i


char = "loveleetcode"
s = solution()
print(s.firstuniqchar(char))