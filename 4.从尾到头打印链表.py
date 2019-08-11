class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listnode):
        # write code here
        ret = []
        head = listnode
        while(head):
            ret.append(head.val)
            head = head.next
        ret.reverse()
        return ret


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    print(Solution().printListFromTailToHead(head))