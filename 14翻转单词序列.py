class Solution:
    def ReverseSentence(self, s):
        # write code here
        ret = s.split(" ")
        ret.reverse()
        return ' '.join(ret)
