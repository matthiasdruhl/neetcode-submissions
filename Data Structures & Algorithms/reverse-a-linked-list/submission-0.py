# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Init pointer to null
        # Init pointer to curr node
        # Init pointer to next node
        # make curr node.next = to null pointer
        # make null pointer = curr
        # make curr node = next pointer
        # make next pointer to next.next

        prev = None
        curr = head 
        if not curr:
            return
        while True:
            if not curr:
                return prev
            temp = curr.next
            curr.next = prev

        
            prev = curr
            
            curr = temp
            
       
        return curr
            
    

            