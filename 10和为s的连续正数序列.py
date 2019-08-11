"""
小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。
但是他并不满足于此,他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。
没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。
现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列?
输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序
思考：S%奇数==0 或者S%偶数==偶数／2 就说明有这个连续序列，但是注意是正数序列，可能会出现越界情况
"""
class Solutions(object):
    def FindContinuousSequence(self, s):
        ret = []
        for k in range(2, s):
            if k % 2 == 1 and s % k == 0:
                tmp = []
                mid = s // k
                if mid - k // 2 > 0:
                    for i in range(mid - k // 2, mid + k // 2 + 1):
                        tmp.append(i)
                    ret.append(tmp[:])
            elif k % 2 == 0 and (s % k) * 2 == k:
                mid = s // k
                tmp = []
                if mid - k // 2 + 1 > 0:
                    for i in range(mid - k // 2 + 1, mid + k // 2 + 1):
                        tmp.append(i)
                    ret.append(tmp[:])
        ret.sort()
        return ret


if __name__ == "__main__":
    print(Solutions().FindContinuousSequence(100))