# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        self.prev = None
        self.curr = head
        while (self.curr != None):
            self.nextTemp = self.curr.next
            self.curr.next = self.prev
            self.prev = self.curr
            self.curr = self.nextTemp
        return self.prev
