class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def Treeheight(self, pRoot):
        if pRoot == None:
            return 0
        if pRoot.left == None and pRoot.right == None:
            return 1
        lh = self.Treeheight(pRoot.left)
        rh = self.Treeheight(pRoot.right)
        return max(rh, lh) + 1

    def IsBalanced_Solution(self, pRoot):
        # write code here
        if pRoot == None:
            return True
        return abs(self.Treeheight(pRoot.left) - self.Treeheight(pRoot.right)) <= 1




if __name__ == "__main__":
    root = TreeNode(3)
    root.left, root.right = TreeNode(9), TreeNode(20)
    root.left.left, root.right.right = TreeNode(15), TreeNode(7)
    root.left.left.left = TreeNode(3)
    print(Solution().IsBalanced_Solution(root))
