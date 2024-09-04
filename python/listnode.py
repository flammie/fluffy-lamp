# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def makelist(l):
    head = ListNode(l[0])
    p = head
    for i in range(1, len(l)):
        node = ListNode(l[i])
        p.next = node
        p = p.next
    return head

def printlist(l):
    p = l
    while p:
        print(p.val)
        p = p.next

