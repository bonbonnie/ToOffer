"""
对于一个给定的字符序列S，请你把其循环左移K位后的序列输出。
"""

class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        if s == '':
            return s
        n = n%len(s)
        return s[n:]+s[0:n]
