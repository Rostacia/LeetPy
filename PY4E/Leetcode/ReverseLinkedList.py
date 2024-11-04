class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode):        
        # Iterative Solution
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
    
    # Recursive Solution
    # if head == None or head.next == None:
    #         return head

    #     reversedSublist = self.reverseList(head.next)
    #     head.next.next = head
    #     head.next = None

    #     return reversedSublist