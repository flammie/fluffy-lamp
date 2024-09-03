
def g(l, r, prefix):
    rv = []
    if l == 0 and r == 0:
        print(f"{prefix=}")
        return [prefix]
    for i in range(1, l+1):
        for rr in g(l-i, r+i, prefix + "(" * i):
            if rr not in rv:
                rv.append(rr)
    for i in range(1, r+1):
        rv = rv + g(l, r-i, prefix + ")" * i)
    print(f"{rv=}")
    return rv

def generateParenthesis(n: int):
    rv = g(n, 0, "")
    return rv


n = 3
print(generateParenthesis(n))
