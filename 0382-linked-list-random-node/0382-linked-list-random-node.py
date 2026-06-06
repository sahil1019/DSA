import random

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def __init__(self, head: ListNode):
        self.head = head

    def getRandom(self) -> int:
        node = self.head
        ans = node.val
        count = 1

        while node:
            if random.randrange(count) == 0:
                ans = node.val

            node = node.next
            count += 1

        return ans