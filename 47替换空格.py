"""
请实现一个函数，将一个字符串中的每个空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
"""


import re
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        return re.sub(" ", "%20", s)

if __name__ == "__main__":
    s = "i am happy"
    print(Solution().replaceSpace(s))