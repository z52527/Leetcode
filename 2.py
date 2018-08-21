# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode(0)
        head = l3
        tmp = 0
        while l1 != None or l2 != None or tmp != 0:
            if l1 != None:
                tmp += l1.val
                l1 = l1.next
            if l2 != None:
                tmp += l2.val
                l2 = l2.next
            l3.next =  ListNode(tmp % 10)
            l3 = l3.next
            tmp = tmp // 10
        return head.next;

        
        