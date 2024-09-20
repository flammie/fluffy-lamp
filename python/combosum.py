
def combosum_r(candidates, target, current, sum, rv):
    for i in candidates:
        print(f"{current=}, {sum=}, {rv=}")
        if sum + i < target:
            current.append(i)
            combosum_r(candidates, target, current, sum + i, rv)
            current.pop()
        elif sum + i == target:
            current.append(i)
            rv.append(sorted(current.copy()))
            current.pop()

def combinationSum(candidates, target):
    rv = []
    combosum_r(candidates, target, [], 0, rv)
    rv2 = []
    for r in rv:
        if r not in rv2:
            rv2.append(r)
    return rv2


print(combinationSum([2, 3, 6, 7], 7))
