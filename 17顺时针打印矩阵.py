class Solutions(object):
    # matrix类型为二维列表，需要返回列表

    def printMatrix1(self, matrix):
        # write code here
        m = len(matrix)
        ans = []
        if m == 0:
            return ans
        n = len(matrix[0])
        # ans = [[0 for i in range(n)] for j in range(m)]
        # print(ans)
        upper_i = 0
        lower_i = m - 1
        left_j = 0
        right_j = n - 1
        num = 1
        i = 0
        j = 0
        right_pointer = 1
        down_pointer = 0
        while num <= m * n:
            ans.append(matrix[i][j])
            if right_pointer == 1:
                if j < right_j:
                    j = j + 1
                else:
                    right_pointer = 0
                    down_pointer = 1
                    upper_i = upper_i + 1
                    i = i + 1
            elif down_pointer == 1:
                if i < lower_i:
                    i = i + 1
                else:
                    right_pointer = -1
                    down_pointer = 0
                    right_j = right_j - 1
                    j = j - 1
            elif right_pointer == -1:
                    if j > left_j:
                        j = j - 1
                    else:
                        right_pointer = 0
                        down_pointer = -1
                        lower_i = lower_i - 1
                        i = i - 1
            elif down_pointer == -1:
                if i > upper_i:
                    i = i - 1
                else:
                    right_pointer = 1
                    down_pointer = 0
                    left_j = left_j + 1
                    j = j + 1
            num = num + 1
        return ans


    # me-wrong
    def printMatrix(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        tr, tc = n-1, m-1
        cnt = 0
        ans = []
        while cnt <= n * m:
            sr = sc = 0
            i, j = sr, sc
            while j < tc:
                ans.append(matrix[i][j])
                cnt += 1
                j += 1
            sr += 1
            i, j = sr, tc
            while i < tr:
                ans.append(matrix[i][j])
                cnt += 1
                i += 1
            tc -= 1
            i, j = tr, tc
            while j >= sc:
                ans.append(matrix[i][j])
                cnt += 1
                j -= 1
            tr -= 1
            i, j = tr, sc
            while i >= sr:
                ans.append(matrix[i][j])
                cnt += 1
                i -= 1
            sc += 1



if __name__ == "__main__":
    d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(Solutions().printMatrix1(d))