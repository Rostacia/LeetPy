class ListNode:
    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
arr = [1,2,3,4,5]
# a = ListNode(1)
# b = ListNode(2)
# c = ListNode(3)
# d = ListNode(4)
# e = ListNode(5)

# a.next = b
# b.next = c
# c.next = d
# d.next = e

nodes = [ListNode(val) for val in arr]

for i in range(len(nodes)-1):
    nodes[i].next = nodes[i+1]
    
head = nodes[0]

def printList(head):
    current = head
    while current:
        print(current.val)
        current = current.next

printList(head)

# def reverseList(head):
#     prev = None
#     current = head
    
#     while current != None:
#         next = current.next
#         current.next = prev
#         prev = current
#         current = next
#     return prev

def reverseList(head):
    if head == None or head.next == None:
        return head
    reversedSublist = reverseList(head.next)
    head.next.next = head
    head.next = None
    return reversedSublist

printList(reverseList(head))