import listnode


def reverseKGroup(head, k):
    prevs = []
    prevtail = None
    newhead = head
    p = head
    while p:
        prevs.append(p)
        if len(prevs) == k + 1:
            p = p.next
            for i in range(len(prevs) - 2, 0, -1):
                prevs[i].next = prevs[i-1]
            if not prevtail:
                newhead = prevs[-2]
                prevtail = prevs[0]
            else:
                prevtail.next = prevs[-2]
                prevtail = prevs[0]
            prevs[0].next = prevs[-1]
            prevs = [prevs[-1]]
        else:
            p = p.next
    if len(prevs) == k:
        for i in range(len(prevs) - 1, 0, -1):
            prevs[i].next = prevs[i-1]
        if not prevtail:
            newhead = prevs[-1]
        else:
            prevtail.next = prevs[-1]
        prevs[0].next = None
    return newhead


l = listnode.makelist([1,2,3,4,5,6,7,8,9,10])
rl = reverseKGroup(l, 5)
listnode.printlist(rl)
