# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    newhead = None
    curr = None
    smallest = 501
    pointers = []
    for l in lists:
        pointers.append(l)
    for p in pointers:
        smallest = min(smallest, p.val)
    for p in pointers:
        if p.val == smallest:
            newhead = p
            break
    pointers.remove(newhead)
    if newhead.next:
        pointers.append(newhead.next)
    print(f"{newhead.val=}")
    curr = newhead
    while pointers:
        smallest = 501
        for p in pointers:
            smallest = min(smallest, p.val)
        newcurr = None
        for p in pointers:
            if p.val == smallest:
                newcurr = p
                break
        curr.next = newcurr
        curr = newcurr
        print(f"{curr.val=}")
        pointers.remove(curr)
        if curr.next:
            pointers.append(curr.next)
    return newhead

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

ll = [[1, 4, 5], [1, 3, 4], [2, 6]]
lists = [makelist(ll[0]), makelist(ll[1]), makelist(ll[2])]
printlist(mergeKLists(lists))

