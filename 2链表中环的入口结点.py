
class Solution(object):
    # 存在环
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None:
            return False
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    # 环的入口
    def EntryNodeOfLoop(self, pHead):
        if pHead == None or pHead.next == None:
            return None
        fast = slow = pHead
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                fast = pHead
                while fast != slow:
                    fast = fast.next
                    slow = slow.next
                return fast
        return None
