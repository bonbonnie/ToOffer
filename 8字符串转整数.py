'''
将一个字符串转换成一个整数，要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0
'''
class Solutions(object):
    def StrToInt(self, s):
        if s == '':
            return 0
        res = 0
        pos = 1
        for i in s:
            if i == '+' or i == '-':
                if s.index(i) == 0:
                    pos = -1 if i == '-' else 1
                else:
                    return 0

            elif '0' <= i <= '9':
                res = res*10 + int(i)

            else:
                return 0

        return pos*res if res else 0


if __name__ == "__main__":
    print(Solutions().StrToInt('-78'))
