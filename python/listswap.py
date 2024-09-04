import listnode


def swapPairs(head):
    p = head
    prev = None
    while p:
        q = p.next
        if q:
            print(f"{p.val=} <-> {q.val=}")
            if not prev:
                head = q
            else:
                prev.next = q
            tmp = q.next
            q.next = p
            prev = p
            p.next = tmp
            p = tmp
        else:
            prev = p
            p = p.next
    return head


l = listnode.makelist([1, 2, 3, 4])
listnode.printlist(swapPairs(l))
