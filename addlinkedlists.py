# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        current_node = ListNode()
        head = current_node
        carry = 0
        while True:

            if l1:
                l1_val = l1.val
            else:
                l1_val = 0
            if l2:
                l2_val = l2.val
            else:
                l2_val = 0

            total = l1_val + l2_val + carry

            carry = 0
            if total > 9:
                carry = 1
                total = total % 10

            if l1:
                l1 = l1.next
            else:
                l1 = None

            if l2:
                l2 = l2.next
            else:
                l2 = None

            current_node.val = total

            if l1 or l2:
                current_node.next = ListNode()
                current_node = current_node.next

            if (not l1) and (not l2):
                if carry:
                    current_node.next = ListNode()
                    current_node = current_node.next
                    current_node.val = 1
                return head