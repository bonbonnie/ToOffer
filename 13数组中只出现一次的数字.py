"""
一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字
思考：用hash；或者位运算
首先利用0 ^ a = a; a^a = 0的性质
两个不相等的元素在位级表示上必定会有一位存在不同，
将数组的所有元素异或得到的结果为不存在重复的两个元素异或的结果，
据异或的结果1所在的最低位，把数字分成两半，每一半里都还有一个出现一次的数据和其他成对出现的数据,
问题就转化为了两个独立的子问题“数组中只有一个数出现一次，其他数都出现了2次，找出这个数字”。
"""

class Solutions(object):
    def FindNumsAppearOnce(self, array):
        d = {}
        res = []
        for n in array:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
        for i, c in d.items():
            if c == 1:
                res.append(i)
        return res

    def FindNumsAppearOnce1(self, array):
        ans, a1, a2, flag = 0, 0, 0, 1
        for num in array:
            ans = ans ^ num
        while (ans):
            if ans % 2 == 0:
                ans = ans >> 1
                flag = flag << 1
            else:
                break
        for num in array:
            if num & flag:
                a1 = a1 ^ num
            else:
                a2 = a2 ^ num
        return a1, a2


if __name__ == "__main__":
    d = [1, 2, 2, 3, 3, 4]
    print(Solutions().FindNumsAppearOnce(d))
    print(Solutions().FindNumsAppearOnce1(d))