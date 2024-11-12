# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # create dummy node pointing to the head of the list
        dummy = ListNode(0, head)
        left = dummy
        right = head

        # move right pointer n nodes from the head of the list
        while n > 0 and right:
            right = right.next
            n -= 1
        
        # shift left nad right pointers until right pointer is at the end of the list
        while right:
            left = left.next
            right = right.next

        # delete node
        left.next = left.next.next
        return dummy.next