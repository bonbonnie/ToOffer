"""
地上有一个m行和n列的方格。
一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，
但是不能进入行坐标和列坐标的数位之和大于k的格子。
例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。
但是，它不能进入方格（35,38），因为3+5+3+8 = 19。
请问该机器人能够达到多少个格子？
思考：dfs+记忆化搜索
"""

class Solution:
    def movingCount(self, threshold, rows, cols):
        memories = set()

        def dfs(i, j):
            def judge(i, j):
                return sum(map(int, list(str(i)))) + sum(map(int, list(str(j)))) <= threshold
            if not judge(i, j) or (i, j) in memories:
                return
            memories.add((i,j))
            if i != rows - 1:
                dfs(i + 1, j)
            if j != cols - 1:
                dfs(i, j + 1)
        dfs(0, 0)
        return len(memories)
