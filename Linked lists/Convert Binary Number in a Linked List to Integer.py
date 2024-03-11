# Definition for singly-linked list.
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head):
        list_node = head
        count = 0
        res = 0

        while list_node:
            count += 1
            list_node = list_node.next

        list_node = head
        for i in range(count - 1, -1, -1):
            res += (list_node.val) * (2 ** i)
            list_node = list_node.next

        return res
