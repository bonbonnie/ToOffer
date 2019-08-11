"""
输入一个递增排序的数组和一个数字S，在数组中查找两个数，
他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
"""

class Solutions(object):
    def FindNumbersWithSum(self, array, tsum):
        d = {}
        res = []
        for c in array:
            if c in d:
                if res == []:
                    res = [c, tsum-c]
                elif res and res[0] * res[1] > c * (tsum-c):
                    res = [c, tsum-c]
            else:
                d[tsum - c] = 1
        return res


    def FindNumbersWithSum1(self, array, tsum):
        memorys = {}
        ret = []
        for num in array:
            if tsum - num in memorys:
                if ret == []:
                    ret = [tsum - num, num]
                elif ret and ret[0] * ret[1] > (tsum - num) * num:
                    ret = [tsum - num, num]
            else:
                memorys[num] = 1
        return ret


if __name__ == "__main__":
    d = [1, 2, 7, 5, 3, 4]
    t = 9
    print(Solutions().FindNumbersWithSum(d, t))