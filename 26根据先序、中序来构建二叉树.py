class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, pre, tin):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if pre==[]:
            return None
        val = pre[0]
        idx = tin.index(val)
        ltin = tin[0:idx]
        rtin = tin[idx+1:]
        lpre = pre[1:1+len(ltin)]
        rpre = pre[1+len(ltin):]
        root = TreeNode(val)
        root.left = self.buildTree(lpre,ltin)
        root.right = self.buildTree(rpre,rtin)
        return root
