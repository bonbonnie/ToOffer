class Solutions(object):
    def fib(self, n):
        if n == 0 or n == 1:
            return n
        mem = [0, 1]
        for i in range(n-1):
            mem[0], mem[1] = mem[1], mem[0] + mem[1]
        return mem[1]

    def Fibonacci(self, n):
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        memories = [1, 1]
        for i in range(n - 2):
            memories.append(memories[-1] + memories[-2])
        return memories[-1]


if __name__ == "__main__":
    print(Solutions().fib(3))
    print(Solutions().Fibonacci(3))