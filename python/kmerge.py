import listnode


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


ll = [[1, 4, 5], [1, 3, 4], [2, 6]]
lists = [listnode.makelist(ll[0]), listnode.makelist(ll[1]), listnode.makelist(ll[2])]
listnode.printlist(mergeKLists(lists))

