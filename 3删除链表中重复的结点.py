'''
Given a sorted linked list, delete all nodes that have duplicate numbers,
leaving only distinct numbers from the original list.
'''


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))


class Solution(object):
    def deleteDuplication(self, pHead):
        pos = pHead
        ret = ListNode(-1)
        tmp = ret
        flag = False
        while pos and pos.next:
            if pos.val == pos.next.val:
                flag = True
                pos.next = pos.next.next
            else:
                if flag:
                    flag = False
                else:
                    tmp.next = ListNode(pos.val)
                    tmp = tmp.next
                pos = pos.next
        if pos and flag == False:
            tmp.next = ListNode(pos.val)
        return ret.next


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    print(Solution().deleteDuplication(head))