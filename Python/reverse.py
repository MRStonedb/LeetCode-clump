
# 实现reverse 
class Solution:
    def reverseString(self, a):
        """
        Do not return anything, modify s in-place instead.
        """

        s = []
        for str in a:
            s.append(str)

        i, j = 0, len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return s

str = "hello"
s = Solution()
print(s.reverseString(str))