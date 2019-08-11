class Solutions(object):
    def jumpFloor(self, n):
        if n == 1 or n == 2:
            return n
        return self.jumpFloor(n-1) + self.jumpFloor(n-2)

    def jumpFloor1(self, number):
        '''
        n = 1 : 1
        n = 2 : 1+1 = 2
        n = 3 : dp[n-2]+dp[n-1]
        '''
        if number == 1 or number == 2:
            return number
        dp = [1, 2]
        for i in range(number - 2):
            dp.append(dp[-1] + dp[-2])
        return dp[-1]


if __name__ == "__main__":
    print(Solutions().jumpFloor(3))
    print(Solutions().jumpFloor1(3))