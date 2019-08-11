class Solutions(object):
    def oddJumpFloor(self, n):
        if n == 1 or n == 2:
            return n
        res = psum = 3
        for i in range(n - 2):
            res = psum + 1
            psum += res
        return res


if __name__ == "__main__":
    print(Solutions().oddJumpFloor(5))