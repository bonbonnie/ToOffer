"""
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
思路：中序遍历的顺序为LVR
则有以下三种情况：
a. 如果该结点存在右子结点，那么该结点的下一个结点是右子结点树上最左子结点
b. 如果该结点不存在右子结点，且它是它父结点的左子结点，那么该结点的下一个结点是它的父结点
c. 如果该结点既不存在右子结点，且也不是它父结点的左子结点，则需要一路向祖先结点搜索，
直到找到一个结点，该结点是其父亲结点的左子结点。
如果这样的结点存在，那么该结点的父亲结点就是我们要找的下一个结点。

"""

class Solution:
    def GetNext(self, pNode):
        # write code here
        # left root right
        if pNode == None:
            return None
        if pNode.right:
            tmp = pNode.right
            while(tmp.left):
                tmp = tmp.left
            return tmp
        p = pNode.next
        while(p and p.right==pNode):
            pNode = p
            p = p.next
        return p
