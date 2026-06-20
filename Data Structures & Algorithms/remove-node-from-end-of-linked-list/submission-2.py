# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        front = head
        back = head

        for i in range(n):
            back = back.next

        prev = None

        while back:
            back = back.next
            prev = front
            front = front.next
        if not prev:
            return front.next

        if front.next:
            prev.next = front.next
        else:
            prev.next = None

        return head
