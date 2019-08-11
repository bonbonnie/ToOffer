"""
数字在排序数组中出现的次数
思考：原来是可以用hash做的，但是因为是排序数组，所以可以用二分查找
"""

class Solutions(object):
    def GetNumberOfK(self, data, k):
        l, r = 0, len(data)-1
        while l <= r:
            m = (r + l) // 2
            if data[m] == k:
               cnt = 1
               rtem = ltem = m
               while rtem < len(data) and data[rtem + 1] == k:
                   cnt += 1
                   rtem += 1

               while ltem > 0 and data[ltem - 1] == k:
                   cnt += 1
                   ltem -= 1

               return cnt

            elif data[m] > k:
                r -= 1
            else:
                l += 1
        return 0


if __name__ == "__main__":
    d = [1, 2, 2, 2, 3, 4]
    k = 2
    print(Solutions().GetNumberOfK(d, k))