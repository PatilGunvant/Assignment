class Solution(object):
    def detectCycle(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow1 = head
                while slow1 != fast:
                    slow1 = slow1.next
                    fast = fast.next
                return slow1
        return None

